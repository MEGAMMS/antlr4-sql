from .ast_nodes import ASTNode

class IdentifierNode(ASTNode):
    def __init__(self, name):
        self.name = name

    def print(self, indent=0):
        print(f"{self._indent(indent)}Identifier: {self.name}")