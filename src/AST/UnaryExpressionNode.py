from __future__ import annotations

from dataclasses import dataclass

from src.AST.ExpressionNode import ExpressionNode


@dataclass
class UnaryExpressionNode(ExpressionNode):
    operator: str
    operand: ExpressionNode

    def _extra(self):
        return f" ({self.operator})"

    def children(self):
        return [self.operand]
