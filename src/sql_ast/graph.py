from __future__ import annotations

from typing import Iterable, List, Tuple

from src.sql_ast.base import ASTNode


def ast_to_dot(node: ASTNode) -> str:
    """Generate a Graphviz DOT description for the AST."""
    lines: List[str] = ["digraph AST {", '  node [shape=box, style="rounded,filled", fillcolor="#eef2ff"];']
    counter = 0
    stack: List[Tuple[str, ASTNode]] = []

    def next_id() -> str:
        nonlocal counter
        counter += 1
        return f"n{counter}"

    def add_node(n: ASTNode) -> str:
        nid = next_id()
        label = n.label().replace('"', '\\"')
        lines.append(f'  {nid} [label="{label}"];')
        return nid

    root = node
    if isinstance(root, list):
        pseudo = ASTNode()
        pseudo_label = "ROOT"
        pseudo_id = "root"
        lines.append(f'  {pseudo_id} [label="{pseudo_label}", shape=ellipse, fillcolor="#dde7ff"];')
        for child in root:
            if isinstance(child, ASTNode):
                cid = add_node(child)
                lines.append(f"  {pseudo_id} -> {cid};")
                stack.append((cid, child))
        lines.append("}")
        return "\n".join(lines)

    root_id = add_node(root)
    stack.append((root_id, root))

    while stack:
        parent_id, parent = stack.pop()
        for child in _iter_children(parent):
            child_id = add_node(child)
            lines.append(f"  {parent_id} -> {child_id};")
            stack.append((child_id, child))

    lines.append("}")
    return "\n".join(lines)


def _iter_children(node: ASTNode) -> Iterable[ASTNode]:
    for child in node.children():
        if child is None:
            continue
        if isinstance(child, list):
            for inner in child:
                if isinstance(inner, ASTNode):
                    yield inner
        elif isinstance(child, ASTNode):
            yield child
