from src.AST.ExpressionNode import ExpressionNode


class UnaryExpressionNode(ExpressionNode):
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand

    def _extra(self):
        return f" ({self.operator})"

    def children(self):
        return [self.operand]
