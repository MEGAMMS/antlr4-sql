# grammar/AST/ast_nodes.py

class ASTNode:
    def print(self, indent=0):
        raise NotImplementedError("print() not implemented in ASTNode")

    def _indent(self, indent):
        return "  " * indent
