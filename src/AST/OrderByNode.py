from src.AST.ast_nodes import ASTNode


class OrderByNode(ASTNode):
    def __init__(self, expression, direction="ASC"):
        self.expression = expression
        self.direction = direction

    def _extra(self):
        return f" ({self.direction})"

    def children(self):
        return [self.expression]
