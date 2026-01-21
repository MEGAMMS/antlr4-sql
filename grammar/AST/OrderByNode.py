from grammar.AST.ast_nodes import ASTNode


class OrderByNode(ASTNode):
    def __init__(self, expression, direction="ASC"):
        self.expression = expression
        self.direction = direction

    def print(self, indent=0):
        print(f"{self._indent(indent)}OrderBy ({self.direction})")
        self.expression.print(indent + 1)
