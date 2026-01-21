# grammar/AST/ast_nodes.py

class ASTNode:
    """Base class for AST nodes with simple tree printing."""

    def children(self):
        """Override to return iterable of child nodes or lists."""
        return []

    def _extra(self):
        """Optional extra info to show next to the node name."""
        return ""

    def print(self, indent=0):
        label = self.__class__.__name__
        extra = self._extra()
        print(f"{self._indent(indent)}{label}{extra}")
        for child in self.children():
            if child is None:
                continue
            if isinstance(child, list):
                for c in child:
                    if c is not None:
                        c.print(indent + 1)
            else:
                child.print(indent + 1)

    def _indent(self, indent):
        return "  " * indent
