from grammar.AST.ExpressionNode import ExpressionNode


class LiteralNode(ExpressionNode):
    def __init__(self, value):
        self.value = value

    def _extra(self):
        return f": {self.value}"
