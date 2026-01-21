from ast_nodes import ASTNode

class ProgramNode(ASTNode):
    def __init__(self, statements):
        self.statements = statements  # list of ASTNode

    def print(self, indent=0):
        print(f"{self._indent(indent)}Program")
        for stmt in self.statements:
            stmt.print(indent + 1)
