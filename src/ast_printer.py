from __future__ import annotations

from typing import Any

from src.AST.ast_nodes import ASTNode, ASTVisitor


class _PrettyPrinter(ASTVisitor):
    def __init__(self, file=None):
        self.file = file

    def print_tree(self, node: Any, indent: int = 0):
        if node is None:
            return
        if isinstance(node, list):
            for child in node:
                self.print_tree(child, indent)
            return
        label = node.label() if isinstance(node, ASTNode) else str(node)
        print(f"{'  '*indent}{label}", file=self.file)
        for child in node.children():
            if child is None:
                continue
            if isinstance(child, list):
                for inner in child:
                    self.print_tree(inner, indent + 1)
            else:
                self.print_tree(child, indent + 1)


class ASTPrinter:
    """Visitor-based pretty printer for ASTs."""

    def __init__(self, file=None):
        self.printer = _PrettyPrinter(file=file)
        self.file = file

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
                self.printer.print_tree(stmt, 1)
        else:
            self.printer.print_tree(node, 0)

        print("\n" + "─" * 80, file=self.file)
