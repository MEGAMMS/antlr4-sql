# ast_nodes.py

from dataclasses import dataclass, field
from typing import List, Optional, Union

# ========== Base Classes ==========
class ASTNode:
    def accept(self, visitor):
        """دلالة Visitor Pattern"""
        method_name = f'visit_{self.__class__.__name__}'
        method = getattr(visitor, method_name, visitor.visit_generic)
        return method(self)

@dataclass
class Statement(ASTNode):
    pass

@dataclass
class Expression(ASTNode):
    pass

# ========== DDL Statements ==========
@dataclass
class CreateTableStatement(Statement):
    table_name: str
    columns: List['ColumnDefinition']
    constraints: List['TableConstraint'] = field(default_factory=list)

@dataclass
class ColumnDefinition:
    name: str
    data_type: 'DataType'
    constraints: List['ColumnConstraint'] = field(default_factory=list)

@dataclass
class DataType:
    name: str
    params: List[int] = field(default_factory=list)  

@dataclass
class ColumnConstraint:
    type: str  # 'NOT_NULL', 'PRIMARY_KEY', 'UNIQUE', 'DEFAULT', 'IDENTITY', 'REFERENCES'
    value: Optional[Expression] = None
    name: Optional[str] = None

@dataclass
class TableConstraint:
    type: str  # 'PRIMARY_KEY', 'FOREIGN_KEY', 'UNIQUE', 'CHECK'
    columns: List[str]
    name: Optional[str] = None
    ref_table: Optional[str] = None
    ref_columns: Optional[List[str]] = None
    check_expr: Optional[Expression] = None

# ========== DML Statements ==========
@dataclass
class SelectStatement(Statement):
    select_list: List['SelectItem']
    from_clause: Optional['TableSource'] = None
    where_clause: Optional[Expression] = None
    group_by: List[Expression] = field(default_factory=list)
    having_clause: Optional[Expression] = None
    order_by: List['OrderByItem'] = field(default_factory=list)
    distinct: bool = False
    top: Optional[int] = None

@dataclass
class SelectItem:
    expression: Expression
    alias: Optional[str] = None

@dataclass
class TableSource:
    source: Union[str, 'SelectStatement']  
    alias: Optional[str] = None

@dataclass
class OrderByItem:
    expression: Expression
    direction: str = 'ASC'

@dataclass
class InsertStatement(Statement):
    table_name: str
    columns: Optional[List[str]] = None
    values: Optional[List[List[Expression]]] = None
    select_query: Optional[SelectStatement] = None

@dataclass
class UpdateStatement(Statement):
    table_name: str
    assignments: List['Assignment']
    where_clause: Optional[Expression] = None

@dataclass
class Assignment:
    column: str
    operator: str  # '=', '+=', '-=', etc.
    value: Expression

@dataclass
class DeleteStatement(Statement):
    table_name: str
    where_clause: Optional[Expression] = None

# ========== Expressions ==========
@dataclass
class BinaryExpression(Expression):
    left: Expression
    operator: str
    right: Expression

@dataclass
class UnaryExpression(Expression):
    operator: str
    operand: Expression

@dataclass
class Literal(Expression):
    value: Union[str, int, float, bool, None]
    type: str  # 'STRING', 'INT', 'FLOAT', 'BOOLEAN', 'NULL'

@dataclass
class ColumnReference(Expression):
    name: str
    table: Optional[str] = None

@dataclass
class VariableReference(Expression):
    name: str  # @local أو @@global

@dataclass
class FunctionCall(Expression):
    name: str
    arguments: List[Expression] = field(default_factory=list)

@dataclass
class CaseExpression(Expression):
    cases: List['CaseWhen']
    else_result: Optional[Expression] = None

@dataclass
class CaseWhen:
    condition: Expression
    result: Expression

@dataclass
class InExpression(Expression):
    value: Expression
    items: Union[List[Expression], SelectStatement]
    not_in: bool = False

@dataclass
class BetweenExpression(Expression):
    value: Expression
    lower: Expression
    upper: Expression
    not_between: bool = False

@dataclass
class LikeExpression(Expression):
    value: Expression
    pattern: Expression
    not_like: bool = False

@dataclass
class IsNullExpression(Expression):
    value: Expression
    not_null: bool = False

# ========== Control Flow ==========
@dataclass
class IfStatement(Statement):
    condition: Expression
    then_branch: List[Statement]
    else_branch: Optional[List[Statement]] = None

@dataclass
class BeginEndBlock(Statement):
    statements: List[Statement]

@dataclass
class TryCatchBlock(Statement):
    try_block: List[Statement]
    catch_block: List[Statement]

# ========== Variable Declaration ==========
@dataclass
class DeclareStatement(Statement):
    variables: List['VariableDeclaration']

@dataclass
class VariableDeclaration:
    name: str
    data_type: DataType
    initial_value: Optional[Expression] = None

@dataclass
class SetStatement(Statement):
    variable: str
    operator: str
    value: Expression

# ========== Other Statements ==========
@dataclass
class UseStatement(Statement):
    database: str

@dataclass
class PrintStatement(Statement):
    expression: Expression

@dataclass
class ExecuteStatement(Statement):
    proc_name: str
    arguments: List[Expression] = field(default_factory=list)
    return_var: Optional[str] = None