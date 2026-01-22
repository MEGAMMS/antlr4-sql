from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional

from .ast_nodes import ASTNode


@dataclass
class SelectNode(ASTNode):
    select_list: List[ASTNode] = field(default_factory=list)
    from_clause: Optional[ASTNode] = None
    joins: List[ASTNode] = field(default_factory=list)
    where_clause: Optional[ASTNode] = None
    group_by: List[ASTNode] = field(default_factory=list)
    having_clause: Optional[ASTNode] = None
    order_by: List[ASTNode] = field(default_factory=list)
    distinct: bool = False
    top: Optional[ASTNode] = None
    with_clause: Optional[ASTNode] = None

    def _extra(self):
        flags = []
        if self.distinct:
            flags.append("DISTINCT")
        if self.top is not None:
            top_val = getattr(self.top, "value", self.top)
            flags.append(f"TOP {top_val}")
        return f" [{' '.join(flags)}]" if flags else ""

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
