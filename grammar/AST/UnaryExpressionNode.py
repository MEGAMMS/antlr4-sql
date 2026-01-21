from grammar.AST.ExpressionNode import ExpressionNode


class UnaryExpressionNode(ExpressionNode):
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand

    def print(self, indent=0):
        print(f"{self._indent(indent)}UnaryExpr ({self.operator})")
        self.operand.print(indent + 1)
