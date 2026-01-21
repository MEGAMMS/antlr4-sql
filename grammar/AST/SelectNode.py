from .ast_nodes import ASTNode


class SelectNode(ASTNode):
    def __init__(
        self,
        select_list,
        from_clause=None,
        joins=None,
        where_clause=None,
        group_by=None,
        having_clause=None,
        order_by=None,
        distinct=False,
        top=None,
        with_clause=None,
    ):
        self.select_list = select_list or []          # list of SelectItem-like nodes
        self.from_clause = from_clause                # TableSourceNode
        self.joins = joins or []                      # list of JoinNode
        self.where_clause = where_clause              # ExpressionNode
        self.group_by = group_by or []                # list of expressions
        self.having_clause = having_clause            # ExpressionNode
        self.order_by = order_by or []                # list of OrderByNode
        self.distinct = distinct
        self.top = top                                # LiteralNode/int
        self.with_clause = with_clause                # WithNode

    def _extra(self):
        flags = []
        if self.distinct:
            flags.append("DISTINCT")
        if self.top is not None:
            top_val = self.top.value if hasattr(self.top, "value") else self.top
            flags.append(f"TOP {top_val}")
        if flags:
            return " [" + " ".join(flags) + "]"
        return ""

    def children(self):
        return [
            self.with_clause,
            self.top,
            self.select_list,
            self.from_clause,
            self.joins,
            self.where_clause,
            self.group_by,
            self.having_clause,
            self.order_by,
        ]
