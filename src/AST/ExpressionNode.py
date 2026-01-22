from __future__ import annotations

from dataclasses import dataclass

from src.AST.ast_nodes import ASTNode


@dataclass
class ExpressionNode(ASTNode):
    """Base class for expressions."""

    pass
