from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List, Optional, Any


class ASTVisitor:
    """Visitor base with dynamic dispatch."""

    def visit(self, node: Optional["ASTNode"]):
        if node is None:
            return None
        method = getattr(self, f"visit_{node.__class__.__name__}", self.generic_visit)
        return method(node)

    def generic_visit(self, node: "ASTNode"):
        for child in node.iter_children():
            self.visit(child)
        return node


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

    def accept(self, visitor: ASTVisitor):
        return visitor.visit(self)


@dataclass
class ExpressionNode(ASTNode):
    """Base class for expressions."""

    pass
