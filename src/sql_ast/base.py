from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List, Any


@dataclass
class ASTNode:
    """Base AST node with visitor + child traversal hooks."""

    def _extra(self) -> str:
        return ""

    def label(self) -> str:
        extra = self._extra()
        return f"{self.__class__.__name__}{extra if extra else ''}"

    def children(self) -> List[Any]:
        """Override to return a list of child nodes or lists."""
        return []

    def iter_children(self) -> Iterable[Any]:
        for child in self.children():
            if child is None:
                continue
            if isinstance(child, list):
                for inner in child:
                    if inner is not None:
                        yield inner
            else:
                yield child


@dataclass
class ExpressionNode(ASTNode):
    """Base class for expressions."""

    pass
