"""
"""

from dataclasses import dataclass, field
from typing import List, Optional, Union, Dict, Any

# ========== Base Classes ==========
class ASTNode:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def __repr__(self):
        return f"{self.__class__.__name__}()"

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
    type: str
    value: Optional[Expression] = None
    name: Optional[str] = None

@dataclass
class TableConstraint:
    type: str
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
    operator: str
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
    type: str

@dataclass
class ColumnReference(Expression):
    name: str
    table: Optional[str] = None

@dataclass
class VariableReference(Expression):
    name: str

@dataclass
class FunctionCall(Expression):
    name: str
    arguments: List[Expression] = field(default_factory=list)

# ========== Control Flow ==========
@dataclass
class IfStatement(Statement):
    condition: Expression
    then_branch: List[Statement]
    else_branch: Optional[List[Statement]] = None

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