from __future__ import annotations

from dataclasses import dataclass

from src.AST.ExpressionNode import ExpressionNode


@dataclass
class LiteralNode(ExpressionNode):
    value: object

    def _extra(self):
        return f": {self.value}"
