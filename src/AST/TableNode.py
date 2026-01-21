from grammar.AST.ast_nodes import ASTNode


class TableNode(ASTNode):
    def __init__(self, parts):
        # parts: list[IdentifierNode] representing schema-qualified name
        self.parts = parts

    def _extra(self):
        name = ".".join(p.name for p in self.parts)
        return f": {name}"

    def children(self):
        return [self.parts]
