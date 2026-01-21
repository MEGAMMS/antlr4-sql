from grammar.AST.ExpressionNode import ExpressionNode
from grammar.AST.ast_nodes import ASTNode


class VariableNode(ExpressionNode):
    def __init__(self, name):
        self.name = name

    def _extra(self):
        return f": {self.name}"


class StarNode(ExpressionNode):
    def _extra(self):
        return ": *"


class FunctionCallNode(ExpressionNode):
    def __init__(self, name, arguments=None):
        self.name = name
        self.arguments = arguments or []

    def _extra(self):
        return f": {self.name}"

    def children(self):
        return [self.arguments]


class BetweenExpressionNode(ExpressionNode):
    def __init__(self, value, low, high, negated=False):
        self.value = value
        self.low = low
        self.high = high
        self.negated = negated

    def _extra(self):
        return " NOT BETWEEN" if self.negated else " BETWEEN"

    def children(self):
        return [self.value, self.low, self.high]


class InExpressionNode(ExpressionNode):
    def __init__(self, value, options, negated=False):
        self.value = value
        self.options = options  # list[ExpressionNode] or SelectNode
        self.negated = negated

    def _extra(self):
        return " NOT IN" if self.negated else " IN"

    def children(self):
        return [self.value, self.options]


class LikeExpressionNode(ExpressionNode):
    def __init__(self, value, pattern, negated=False):
        self.value = value
        self.pattern = pattern
        self.negated = negated

    def _extra(self):
        return " NOT LIKE" if self.negated else " LIKE"

    def children(self):
        return [self.value, self.pattern]


class IsNullExpressionNode(ExpressionNode):
    def __init__(self, value, negated=False):
        self.value = value
        self.negated = negated

    def _extra(self):
        return " IS NOT NULL" if self.negated else " IS NULL"

    def children(self):
        return [self.value]


class ExistsExpressionNode(ExpressionNode):
    def __init__(self, subquery):
        self.subquery = subquery

    def _extra(self):
        return " EXISTS"

    def children(self):
        return [self.subquery]


class CaseExpressionNode(ExpressionNode):
    def __init__(self, when_clauses, else_expr=None):
        self.when_clauses = when_clauses or []
        self.else_expr = else_expr

    def children(self):
        return [self.when_clauses, self.else_expr]


class WhenClauseNode(ASTNode):
    def __init__(self, condition, result):
        self.condition = condition
        self.result = result

    def _extra(self):
        return ": WHEN"

    def children(self):
        return [self.condition, self.result]
