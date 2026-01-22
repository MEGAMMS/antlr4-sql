from antlr4 import CommonTokenStream, FileStream, InputStream, Token
from antlr4.error.ErrorListener import ErrorListener

from src.antlr_generated.grammar.SQLLexer import SQLLexer
from src.antlr_generated.grammar.SQLParser import SQLParser
from src.ast_builder import ASTBuilder
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
