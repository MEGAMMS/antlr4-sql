from .ast_nodes import ASTNode

class IdentifierNode(ASTNode):
    def __init__(self, name):
        self.name = name

    def _extra(self):
        return f": {self.name}"
