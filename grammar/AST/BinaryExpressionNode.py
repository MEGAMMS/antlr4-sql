from grammar.AST.ExpressionNode import ExpressionNode


class BinaryExpressionNode(ExpressionNode):
    def __init__(self, operator, left, right):
        self.operator = operator
        self.left = left
        self.right = right

    def print(self, indent=0):
        print(f"{self._indent(indent)}BinaryExpr ({self.operator})")
        self.left.print(indent + 1)
        self.right.print(indent + 1)
