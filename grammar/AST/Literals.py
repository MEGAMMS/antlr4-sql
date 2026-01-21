from grammar.AST.ExpressionNode import ExpressionNode


class LiteralNode(ExpressionNode):
    def __init__(self, value):
        self.value = value

    def print(self, indent=0):
        print(f"{self._indent(indent)}Literal: {self.value}")
