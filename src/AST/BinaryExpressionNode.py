from __future__ import annotations

from dataclasses import dataclass

from src.AST.ExpressionNode import ExpressionNode


@dataclass
class BinaryExpressionNode(ExpressionNode):
    operator: str
    left: ExpressionNode
    right: ExpressionNode

    def _extra(self):
        return f" ({self.operator})"

    def children(self):
        return [self.left, self.right]
