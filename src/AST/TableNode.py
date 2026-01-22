from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

from src.AST.ast_nodes import ASTNode
from src.AST.IdentifierNode import IdentifierNode


@dataclass
class TableNode(ASTNode):
    parts: List[IdentifierNode] = field(default_factory=list)  # schema-qualified identifiers

    def _extra(self):
        name = ".".join(p.name for p in self.parts)
        return f": {name}"

    def children(self):
        return [self.parts]
