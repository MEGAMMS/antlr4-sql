from __future__ import annotations

from dataclasses import dataclass

from .ast_nodes import ASTNode


@dataclass
class IdentifierNode(ASTNode):
    name: str

    def _extra(self):
        return f": {self.name}"
