from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

from .ast_nodes import ASTNode


@dataclass
class ProgramNode(ASTNode):
    statements: List[ASTNode] = field(default_factory=list)

    def children(self):
        return [self.statements]
