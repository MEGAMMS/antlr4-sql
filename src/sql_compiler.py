import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from antlr4 import CommonTokenStream, InputStream, Token
from antlr4.error.ErrorListener import ErrorListener

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
for path in (ROOT, SRC):
    str_path = str(path)
    if str_path not in sys.path:
        sys.path.insert(0, str_path)

GRAMMAR_DIR = ROOT / "grammar"
OUT_DIR = SRC / "antlr_generated"
ANTLR_JAR = ROOT / "tools" / "antlr" / "antlr-4.13.2-complete.jar"
_GRAMMAR_SOURCES = [GRAMMAR_DIR / "SQLLexer.g4", GRAMMAR_DIR / "SQLParser.g4"]
_GENERATED_TARGETS = [OUT_DIR / "SQLLexer.py", OUT_DIR / "SQLParser.py"]
_antlr_ready = False


def _outputs_are_fresh() -> bool:
    try:
        latest_grammar = max(path.stat().st_mtime for path in _GRAMMAR_SOURCES)
        oldest_generated = min(path.stat().st_mtime for path in _GENERATED_TARGETS)
    except FileNotFoundError:
        return False
    return oldest_generated >= latest_grammar


def ensure_antlr_generated(force: bool = False) -> None:
    """
    Regenerate ANTLR outputs if they are missing or stale. When force=True,
    regeneration happens on every call.
    """
    global _antlr_ready
    if _antlr_ready and not force:
        return

    needs_regen = force or not _outputs_are_fresh()
    if not needs_regen:
        _antlr_ready = True
        return

    if not ANTLR_JAR.exists():
        raise RuntimeError(f"Missing ANTLR jar at {ANTLR_JAR}")

    print("Regenerating ANTLR outputs...")

    tmp_root = Path(tempfile.mkdtemp(prefix="antlr_gen_", dir=OUT_DIR.parent))
    tmp_root.mkdir(parents=True, exist_ok=True)
    (tmp_root / "__init__.py").touch()

    lexer_cmd = [
        "java",
        "-jar",
        str(ANTLR_JAR),
        "-Xexact-output-dir",
        "-Dlanguage=Python3",
        "-visitor",
        "-no-listener",
        str(GRAMMAR_DIR / "SQLLexer.g4"),
        "-o",
        str(tmp_root),
    ]
    parser_cmd = [
        "java",
        "-jar",
        str(ANTLR_JAR),
        "-Xexact-output-dir",
        "-Dlanguage=Python3",
        "-visitor",
        "-no-listener",
        "-lib",
        str(tmp_root),
        str(GRAMMAR_DIR / "SQLParser.g4"),
        "-o",
        str(tmp_root),
    ]

    try:
        subprocess.run(lexer_cmd, check=True, cwd=ROOT)
        subprocess.run(parser_cmd, check=True, cwd=ROOT)
    except (subprocess.CalledProcessError, FileNotFoundError) as exc:  # pragma: no cover - setup failure
        shutil.rmtree(tmp_root, ignore_errors=True)
        raise RuntimeError(
            "Failed to regenerate ANTLR outputs; ensure Java 17+ is installed and the ANTLR jar is present."
        ) from exc
    else:
        shutil.rmtree(OUT_DIR, ignore_errors=True)
        shutil.move(str(tmp_root), str(OUT_DIR))

    _antlr_ready = True


ensure_antlr_generated()

from src.antlr_generated.SQLLexer import SQLLexer
from src.antlr_generated.SQLParser import SQLParser
from src.sql_ast.builder import ASTBuilder
from src.tools import ASTPrinter, print_parse_tree, token_type_name


class CollectingErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f"line {line}:{column} {msg}")


class SQLCompiler:
    @staticmethod
    def run_file(path: str, show_parse_tree: bool = False, show_tokens: bool = True):
        with open(path, encoding="utf-8") as f:
            sql = f.read()
        return SQLCompiler.run_string(sql, label=path, show_parse_tree=show_parse_tree, show_tokens=show_tokens)

    @staticmethod
    def run_string(sql: str, label: str = "<input>", show_parse_tree: bool = False, show_tokens: bool = True):
        print(f"\n===== SQL INPUT ({label}) =====")
        print(sql.strip())
        print("=" * 60)

        input_stream = InputStream(sql)

        # Lexer
        lexer = SQLLexer(input_stream)
        lex_err = CollectingErrorListener()
        lexer.removeErrorListeners()
        lexer.addErrorListener(lex_err)
        token_stream = CommonTokenStream(lexer)
        token_stream.fill()

        tokens = [t for t in token_stream.tokens if t.type != Token.EOF]
        if show_tokens:
            print(f"Tokens ({len(tokens)} total):")
            for i, t in enumerate(tokens[:50], start=1):
                name = token_type_name(lexer, t.type)
                text = t.text.replace("\n", "\\n").replace("\r", "\\r")
                print(f"{i:>3}: {name:<15} '{text}'")
            if len(tokens) > 50:
                print("... (truncated)")
        if lex_err.errors:
            print("Lexer errors:")
            for e in lex_err.errors:
                print("  ", e)
            return None

        # Parser
        parser = SQLParser(token_stream)
        parse_err = CollectingErrorListener()
        parser.removeErrorListeners()
        parser.addErrorListener(parse_err)
        tree = parser.root()

        if parse_err.errors:
            print("Parser errors:")
            for e in parse_err.errors:
                print("  ", e)
            return None

        if show_parse_tree:
            print_parse_tree(tree, parser, max_depth=8)

        # AST
        builder = ASTBuilder()
        ast = builder.visit(tree)
        ASTPrinter().print(ast)
        return ast


if __name__ == "__main__":
    import sys

    paths = sys.argv[1:] or []
    if not paths:
        SQLCompiler.run_string("SELECT 1 + 1;", label="inline")
    else:
        for p in paths:
            SQLCompiler.run_file(p)
