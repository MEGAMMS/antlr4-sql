from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional

from src.ast.base import ASTNode
from src.ast.expressions import ExpressionNode


@dataclass
class IdentifierNode(ASTNode):
    name: str

    def _extra(self):
        return f": {self.name}"


@dataclass
class LiteralNode(ExpressionNode):
    value: object

    def _extra(self):
        return f": {self.value}"


@dataclass
class TableNode(ASTNode):
    parts: List[IdentifierNode] = field(default_factory=list)

    def _extra(self):
        name = ".".join(p.name for p in self.parts)
        return f": {name}"

    def children(self):
        return [self.parts]


@dataclass
class OrderByNode(ASTNode):
    expression: ASTNode
    direction: str = "ASC"

    def _extra(self):
        return f" ({self.direction})"

    def children(self):
        return [self.expression]


@dataclass
class WithNode(ASTNode):
    ctes: List["CteNode"] = field(default_factory=list)

    def children(self):
        return [self.ctes]


@dataclass
class CteNode(ASTNode):
    name: ASTNode
    columns: List[ASTNode] = field(default_factory=list)
    query: ASTNode | None = None

    def _extra(self):
        display = getattr(self.name, "name", self.name)
        return f": {display}"

    def children(self):
        return [self.columns, self.query]


@dataclass
class SelectItemNode(ASTNode):
    expression: ASTNode
    alias: Optional[str] = None

    def _extra(self):
        return f" AS {self.alias}" if self.alias else ""

    def children(self):
        return [self.expression]


@dataclass
class SelectVarAssignNode(ASTNode):
    variable: ASTNode
    operator: str
    expression: ASTNode

    def _extra(self):
        return f" {self.operator}"

    def children(self):
        return [self.variable, self.expression]


@dataclass
class TableSourceNode(ASTNode):
    source: ASTNode
    alias: Optional[ASTNode] = None

    def _extra(self):
        return f" AS {self.alias.name}" if self.alias else ""

    def children(self):
        return [self.source]


@dataclass
class JoinNode(ASTNode):
    join_type: Optional[str]
    table_source: TableSourceNode
    condition: ASTNode

    def _extra(self):
        jt = self.join_type or "JOIN"
        return f" ({jt})"

    def children(self):
        return [self.table_source, self.condition]


@dataclass
class ValueListNode(ASTNode):
    values: List[ASTNode] = field(default_factory=list)

    def children(self):
        return [self.values]


@dataclass
class InsertStatement(ASTNode):
    table: ASTNode
    columns: List[ASTNode] = field(default_factory=list)
    values: List[ValueListNode] = field(default_factory=list)
    select_query: Optional[ASTNode] = None
    with_clause: Optional[WithNode] = None

    def children(self):
        return [self.with_clause, self.table, self.columns, self.values, self.select_query]


@dataclass
class AssignmentNode(ASTNode):
    target: ASTNode
    operator: str
    value: ASTNode

    def _extra(self):
        return f" ({self.operator})"

    def children(self):
        return [self.target, self.value]


@dataclass
class UpdateStatement(ASTNode):
    table: ASTNode
    assignments: List[AssignmentNode] = field(default_factory=list)
    where_clause: Optional[ASTNode] = None
    with_clause: Optional[WithNode] = None

    def children(self):
        return [self.with_clause, self.table, self.assignments, self.where_clause]


@dataclass
class DeleteStatement(ASTNode):
    table: ASTNode
    where_clause: Optional[ASTNode] = None
    with_clause: Optional[WithNode] = None

    def children(self):
        return [self.with_clause, self.table, self.where_clause]


@dataclass
class DataTypeNode(ASTNode):
    name: str
    params: List[ASTNode] = field(default_factory=list)

    def _extra(self):
        if self.params:
            def _param_text(p):
                if hasattr(p, "value"):
                    return p.value
                if hasattr(p, "name"):
                    return p.name
                return p

            joined = ", ".join(str(_param_text(p)) for p in self.params)
            return f": {self.name}({joined})"
        return f": {self.name}"

    def children(self):
        return [self.params]


@dataclass
class ColumnConstraintNode(ASTNode):
    kind: str
    details: Optional[ASTNode] = None

    def _extra(self):
        return f": {self.kind}"

    def children(self):
        return [self.details] if self.details else []


@dataclass
class ColumnDefNode(ASTNode):
    name: ASTNode
    data_type: DataTypeNode
    constraints: List[ColumnConstraintNode] = field(default_factory=list)

    def _extra(self):
        return f": {self.name.name}"

    def children(self):
        return [self.data_type, self.constraints]


@dataclass
class TableReferenceNode(ASTNode):
    table: ASTNode
    columns: List[ASTNode] = field(default_factory=list)

    def children(self):
        return [self.table, self.columns]


@dataclass
class TableConstraintNode(ASTNode):
    kind: str
    columns: List[ASTNode] = field(default_factory=list)
    reference: Optional[TableReferenceNode] = None
    condition: Optional[ASTNode] = None
    name: Optional[ASTNode] = None

    def _extra(self):
        parts = [self.kind]
        if self.name:
            parts.append(f"CONSTRAINT {self.name.name}")
        return ": " + " ".join(parts)

    def children(self):
        return [self.columns, self.reference, self.condition]


@dataclass
class CreateTableNode(ASTNode):
    table: ASTNode
    elements: List[ASTNode] = field(default_factory=list)

    def children(self):
        return [self.table, self.elements]


@dataclass
class AlterTableNode(ASTNode):
    table: ASTNode
    action: str
    detail: ASTNode

    def _extra(self):
        return f": {self.action}"

    def children(self):
        return [self.table, self.detail]


@dataclass
class DropStatementNode(ASTNode):
    object_type: str
    name: ASTNode

    def _extra(self):
        return f": DROP {self.object_type}"

    def children(self):
        return [self.name]


@dataclass
class TruncateStatementNode(ASTNode):
    table: ASTNode

    def _extra(self):
        return ": TRUNCATE"

    def children(self):
        return [self.table]


@dataclass
class UseStatementNode(ASTNode):
    database: ASTNode

    def _extra(self):
        return f": {self.database.name}"


@dataclass
class PrintStatementNode(ASTNode):
    expression: ASTNode

    def children(self):
        return [self.expression]


@dataclass
class SetStatementNode(ASTNode):
    variable: ASTNode
    operator: str
    expression: ASTNode

    def _extra(self):
        return f": {self.operator}"

    def children(self):
        return [self.variable, self.expression]


@dataclass
class DeclareStatementNode(ASTNode):
    declarations: List["DeclaredVariableNode"] = field(default_factory=list)

    def _extra(self):
        return f": {len(self.declarations)} item(s)"

    def children(self):
        return [self.declarations]


@dataclass
class DeclaredVariableNode(ASTNode):
    name: ASTNode
    data_type: DataTypeNode
    default_value: Optional[ASTNode] = None

    def _extra(self):
        display = getattr(self.name, "name", self.name)
        return f": {display}"

    def children(self):
        return [self.data_type, self.default_value]


@dataclass
class CursorDeclareNode(ASTNode):
    name: ASTNode
    select_query: ASTNode

    def _extra(self):
        return f": {self.name.name}"

    def children(self):
        return [self.select_query]


@dataclass
class OpenCursorNode(ASTNode):
    name: ASTNode

    def _extra(self):
        return f": {self.name.name}"


@dataclass
class FetchCursorNode(ASTNode):
    name: ASTNode
    variables: List[ASTNode] = field(default_factory=list)

    def _extra(self):
        return f": {self.name.name}"

    def children(self):
        return [self.variables]


@dataclass
class CloseCursorNode(ASTNode):
    name: ASTNode

    def _extra(self):
        return f": {self.name.name}"


@dataclass
class DeallocateCursorNode(ASTNode):
    name: ASTNode

    def _extra(self):
        return f": {self.name.name}"


@dataclass
class BlockNode(ASTNode):
    statements: List[ASTNode] = field(default_factory=list)

    def children(self):
        return [self.statements]


@dataclass
class IfStatementNode(ASTNode):
    condition: ASTNode
    then_block: ASTNode
    else_block: Optional[ASTNode] = None

    def children(self):
        return [self.condition, self.then_block, self.else_block]


@dataclass
class TryCatchNode(ASTNode):
    try_block: ASTNode
    catch_block: ASTNode

    def children(self):
        return [self.try_block, self.catch_block]


@dataclass
class ExecuteNode(ASTNode):
    target: ASTNode
    arguments: List[ASTNode] = field(default_factory=list)
    output_variable: Optional[ASTNode] = None

    def _extra(self):
        return f": EXEC" + (f" -> {self.output_variable.name}" if self.output_variable else "")

    def children(self):
        return [self.target, self.arguments]


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


@dataclass
class ProgramNode(ASTNode):
    statements: List[ASTNode] = field(default_factory=list)

    def children(self):
        return [self.statements]
