from __future__ import annotations

from dataclasses import dataclass

from src.AST.ast_nodes import ASTNode


@dataclass
class OrderByNode(ASTNode):
    expression: ASTNode
    direction: str = "ASC"

    def _extra(self):
        return f" ({self.direction})"

    def children(self):
        return [self.expression]
