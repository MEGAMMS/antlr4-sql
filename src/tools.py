from __future__ import annotations

from antlr4 import CommonTokenStream, FileStream, Token
from antlr4.error.ErrorListener import ErrorListener
from antlr4.tree.Tree import TerminalNodeImpl, ErrorNodeImpl
from antlr4 import ParserRuleContext

from src.antlr_generated.SQLLexer import SQLLexer
from src.sql_ast.base import ASTNode


class CollectingErrorListener(ErrorListener):
    def __init__(self):
        self.errors: list[str] = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f"line {line}:{column} {msg}")


def token_type_name(lexer: SQLLexer, ttype: int) -> str:
    if ttype == Token.EOF:
        return "EOF"
    try:
        sym = lexer.symbolicNames[ttype]
        if sym and not sym.startswith("T__"):
            return sym
    except Exception:
        pass
    try:
        vocab = lexer.getVocabulary()
        name = vocab.getDisplayName(ttype)
        return name.strip("'")
    except Exception:
        return str(ttype)


def tokenize_file(path: str, strict: bool = False):
    lexer = SQLLexer(FileStream(path, encoding="utf-8"))

    err = CollectingErrorListener()
    lexer.removeErrorListeners()
    lexer.addErrorListener(err)

    stream = CommonTokenStream(lexer)
    stream.fill()

    if strict and err.errors:
        raise SyntaxError(err.errors[0])

    tokens = []
    for t in stream.tokens:
        if t.type == Token.EOF:
            break
        tokens.append(t)

    return tokens, err.errors, lexer


class TreePrinter:
    def __init__(self, parser, show_tokens=True):
        self.parser = parser
        self.show_tokens = show_tokens

    def print_tree(self, node, indent=0, max_depth=None, is_last=True):
        if max_depth is not None and indent >= max_depth:
            self._print_indented("└─ ...", indent, is_last)
            return

        prefix = "│   " * (indent - 1) if indent > 0 else ""
        if indent > 0:
            prefix += "└── " if is_last else "├── "

        if isinstance(node, TerminalNodeImpl):
            if not self.show_tokens:
                return
            symbol = node.getSymbol()
            token_type = symbol.type

            if token_type == Token.EOF:
                token_name = "EOF"
            elif hasattr(self.parser, "symbolicNames") and token_type < len(self.parser.symbolicNames):
                token_name = self.parser.symbolicNames[token_type] or f"<{token_type}>"
            else:
                token_name = f"<{token_type}>"

            text = symbol.text.replace("\n", "\\n").replace("\r", "\\r")
            print(f"{prefix}{token_name}: '{text}'")

        elif isinstance(node, ParserRuleContext):
            rule_name = self._get_rule_name(node)
            print(f"{prefix}[{rule_name}]")
            if hasattr(node, "children") and node.children:
                child_count = len(node.children)
                for i, child in enumerate(node.children):
                    child_is_last = i == child_count - 1
                    self.print_tree(child, indent + 1, max_depth, child_is_last)

        elif isinstance(node, ErrorNodeImpl):
            print(f"{prefix}⚠ ERROR: {node}")
        else:
            print(f"{prefix}{type(node).__name__}")

    def _print_indented(self, text, indent, is_last):
        prefix = "│   " * (indent - 1) if indent > 0 else ""
        if indent > 0:
            prefix += "└── " if is_last else "├── "
        print(f"{prefix}{text}")

    def _get_rule_name(self, ctx):
        if hasattr(ctx, "getRuleIndex") and hasattr(self.parser, "ruleNames"):
            rule_index = ctx.getRuleIndex()
            if rule_index < len(self.parser.ruleNames):
                return self.parser.ruleNames[rule_index]
        return type(ctx).__name__


def print_parse_tree(tree, parser, max_depth=5):
    print("\n" + "🌳 " * 10)
    print("PARSE TREE")
    print("🌳 " * 10)
    printer = TreePrinter(parser, show_tokens=True)
    printer.print_tree(tree, max_depth=max_depth)
    print("─" * 80)


class ASTPrinter:
    """Visitor-based pretty printer for ASTs."""

    def __init__(self, file=None):
        self.file = file

    def _print_tree(self, node, indent: int = 0):
        if node is None:
            return
        if isinstance(node, list):
            for child in node:
                self._print_tree(child, indent)
            return
        label = node.label() if isinstance(node, ASTNode) else str(node)
        print(f"{'  '*indent}{label}", file=self.file)
        for child in node.children():
            if child is None:
                continue
            if isinstance(child, list):
                for inner in child:
                    self._print_tree(inner, indent + 1)
            else:
                self._print_tree(child, indent + 1)

    def print(self, node):
        if node is None:
            print("🌳 AST: empty", file=self.file)
            return

        print("\n" + "🌳 " * 10, file=self.file)
        print("✨ AST Tree", file=self.file)
        print("🌳 " * 10, file=self.file)

        if isinstance(node, list):
            for i, stmt in enumerate(node, start=1):
                print(f"\n📄 Statement {i}:", file=self.file)
                self._print_tree(stmt, 1)
        else:
            self._print_tree(node, 0)

        print("\n" + "─" * 80, file=self.file)
