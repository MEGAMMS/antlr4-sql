from .ast_nodes import ASTNode

class SelectNode(ASTNode):
    def __init__(self, select_list, from_clause=None, where_clause=None, order_by=None):
        self.select_list = select_list        # list of ASTNode
        self.from_clause = from_clause        # TableNode
        self.where_clause = where_clause      # ExpressionNode
        self.order_by = order_by              # list of OrderByNode

    def print(self, indent=0):
        print(f"{self._indent(indent)}Select")
        
        print(f"{self._indent(indent+1)}Columns")
        for col in self.select_list:
            col.print(indent + 2)

        if self.from_clause:
            print(f"{self._indent(indent+1)}From")
            self.from_clause.print(indent + 2)

        if self.where_clause:
            print(f"{self._indent(indent+1)}Where")
            self.where_clause.print(indent + 2)

        if self.order_by:
            print(f"{self._indent(indent+1)}OrderBy")
            for item in self.order_by:
                item.print(indent + 2)
