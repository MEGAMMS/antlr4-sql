from grammar.AST.ast_nodes import ASTNode


class TableNode(ASTNode):
    def __init__(self, name):
        self.name = name  # IdentifierNode

    def print(self, indent=0):
        print(f"{self._indent(indent)}Table")
        self.name.print(indent + 1)