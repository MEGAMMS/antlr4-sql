from grammar.AST.ExpressionNode import ExpressionNode


class BinaryExpressionNode(ExpressionNode):
    def __init__(self, operator, left, right):
        self.operator = operator
        self.left = left
        self.right = right

    def _extra(self):
        return f" ({self.operator})"

    def children(self):
        return [self.left, self.right]
