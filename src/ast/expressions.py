from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Union

from src.ast.base import ExpressionNode, ASTNode


@dataclass
class BinaryExpressionNode(ExpressionNode):
    operator: str
    left: ExpressionNode
    right: ExpressionNode

    def _extra(self):
        return f" ({self.operator})"

    def children(self):
        return [self.left, self.right]


@dataclass
class UnaryExpressionNode(ExpressionNode):
    operator: str
    operand: ExpressionNode

    def _extra(self):
        return f" ({self.operator})"

    def children(self):
        return [self.operand]


@dataclass
class VariableNode(ExpressionNode):
    name: str

    def _extra(self):
        return f": {self.name}"


@dataclass
class StarNode(ExpressionNode):
    def _extra(self):
        return ": *"


@dataclass
class FunctionCallNode(ExpressionNode):
    name: str
    arguments: List[ExpressionNode] = field(default_factory=list)

    def _extra(self):
        return f": {self.name}"

    def children(self):
        return [self.arguments]


@dataclass
class BetweenExpressionNode(ExpressionNode):
    value: ExpressionNode
    low: ExpressionNode
    high: ExpressionNode
    negated: bool = False

    def _extra(self):
        return " NOT BETWEEN" if self.negated else " BETWEEN"

    def children(self):
        return [self.value, self.low, self.high]


@dataclass
class InExpressionNode(ExpressionNode):
    value: ExpressionNode
    options: Union[List[ExpressionNode], ASTNode]
    negated: bool = False

    def _extra(self):
        return " NOT IN" if self.negated else " IN"

    def children(self):
        return [self.value, self.options]


@dataclass
class LikeExpressionNode(ExpressionNode):
    value: ExpressionNode
    pattern: ExpressionNode
    negated: bool = False

    def _extra(self):
        return " NOT LIKE" if self.negated else " LIKE"

    def children(self):
        return [self.value, self.pattern]


@dataclass
class IsNullExpressionNode(ExpressionNode):
    value: ExpressionNode
    negated: bool = False

    def _extra(self):
        return " IS NOT NULL" if self.negated else " IS NULL"

    def children(self):
        return [self.value]


@dataclass
class ExistsExpressionNode(ExpressionNode):
    subquery: ASTNode

    def _extra(self):
        return " EXISTS"

    def children(self):
        return [self.subquery]


@dataclass
class CaseExpressionNode(ExpressionNode):
    when_clauses: List["WhenClauseNode"] = field(default_factory=list)
    else_expr: ExpressionNode | None = None

    def children(self):
        return [self.when_clauses, self.else_expr]


@dataclass
class WhenClauseNode(ASTNode):
    condition: ExpressionNode
    result: ExpressionNode

    def _extra(self):
        return ": WHEN"

    def children(self):
        return [self.condition, self.result]
