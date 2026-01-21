from .ast_nodes import ASTNode

class ProgramNode(ASTNode):
    def __init__(self, statements):
        self.statements = statements  # list of ASTNode

    def children(self):
        return [self.statements]
