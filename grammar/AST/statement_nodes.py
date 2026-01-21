from grammar.AST.ast_nodes import ASTNode


class WithNode(ASTNode):
    def __init__(self, ctes):
        self.ctes = ctes or []

    def children(self):
        return [self.ctes]


class CteNode(ASTNode):
    def __init__(self, name, columns, query):
        self.name = name
        self.columns = columns or []
        self.query = query

    def _extra(self):
        return f": {self.name.name}"

    def children(self):
        return [self.columns, self.query]


class SelectItemNode(ASTNode):
    def __init__(self, expression, alias=None):
        self.expression = expression
        self.alias = alias

    def _extra(self):
        return f" AS {self.alias}" if self.alias else ""

    def children(self):
        return [self.expression]


class SelectVarAssignNode(ASTNode):
    def __init__(self, variable, operator, expression):
        self.variable = variable
        self.operator = operator
        self.expression = expression

    def _extra(self):
        return f" {self.operator}"

    def children(self):
        return [self.variable, self.expression]


class TableSourceNode(ASTNode):
    def __init__(self, source, alias=None):
        self.source = source
        self.alias = alias

    def _extra(self):
        return f" AS {self.alias.name}" if self.alias else ""

    def children(self):
        return [self.source]


class JoinNode(ASTNode):
    def __init__(self, join_type, table_source, condition):
        self.join_type = join_type
        self.table_source = table_source
        self.condition = condition

    def _extra(self):
        jt = self.join_type or "JOIN"
        return f" ({jt})"

    def children(self):
        return [self.table_source, self.condition]


class ValueListNode(ASTNode):
    def __init__(self, values):
        self.values = values or []

    def children(self):
        return [self.values]


class InsertStatement(ASTNode):
    def __init__(self, table, columns, values=None, select_query=None, with_clause=None):
        self.table = table
        self.columns = columns or []
        self.values = values or []
        self.select_query = select_query
        self.with_clause = with_clause

    def children(self):
        return [self.with_clause, self.table, self.columns, self.values, self.select_query]


class AssignmentNode(ASTNode):
    def __init__(self, target, operator, value):
        self.target = target
        self.operator = operator
        self.value = value

    def _extra(self):
        return f" ({self.operator})"

    def children(self):
        return [self.target, self.value]


class UpdateStatement(ASTNode):
    def __init__(self, table, assignments, where_clause=None, with_clause=None):
        self.table = table
        self.assignments = assignments or []
        self.where_clause = where_clause
        self.with_clause = with_clause

    def children(self):
        return [self.with_clause, self.table, self.assignments, self.where_clause]


class DeleteStatement(ASTNode):
    def __init__(self, table, where_clause=None, with_clause=None):
        self.table = table
        self.where_clause = where_clause
        self.with_clause = with_clause

    def children(self):
        return [self.with_clause, self.table, self.where_clause]


class DataTypeNode(ASTNode):
    def __init__(self, name, params=None):
        self.name = name
        self.params = params or []

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


class ColumnConstraintNode(ASTNode):
    def __init__(self, kind, details=None):
        self.kind = kind
        self.details = details

    def _extra(self):
        return f": {self.kind}"

    def children(self):
        return [self.details] if self.details else []


class ColumnDefNode(ASTNode):
    def __init__(self, name, data_type, constraints=None):
        self.name = name
        self.data_type = data_type
        self.constraints = constraints or []

    def _extra(self):
        return f": {self.name.name}"

    def children(self):
        return [self.data_type, self.constraints]


class TableConstraintNode(ASTNode):
    def __init__(self, kind, columns=None, reference=None, condition=None, name=None):
        self.kind = kind
        self.columns = columns or []
        self.reference = reference
        self.condition = condition
        self.name = name

    def _extra(self):
        parts = [self.kind]
        if self.name:
            parts.append(f"CONSTRAINT {self.name.name}")
        return ": " + " ".join(parts)

    def children(self):
        return [self.columns, self.reference, self.condition]


class CreateTableNode(ASTNode):
    def __init__(self, table, elements):
        self.table = table
        self.elements = elements or []

    def children(self):
        return [self.table, self.elements]


class AlterTableNode(ASTNode):
    def __init__(self, table, action, detail):
        self.table = table
        self.action = action
        self.detail = detail

    def _extra(self):
        return f": {self.action}"

    def children(self):
        return [self.table, self.detail]


class DropStatementNode(ASTNode):
    def __init__(self, object_type, name):
        self.object_type = object_type
        self.name = name

    def _extra(self):
        return f": DROP {self.object_type}"

    def children(self):
        return [self.name]


class TruncateStatementNode(ASTNode):
    def __init__(self, table):
        self.table = table

    def _extra(self):
        return ": TRUNCATE"

    def children(self):
        return [self.table]


class UseStatementNode(ASTNode):
    def __init__(self, database):
        self.database = database

    def _extra(self):
        return f": {self.database.name}"


class PrintStatementNode(ASTNode):
    def __init__(self, expression):
        self.expression = expression

    def children(self):
        return [self.expression]


class SetStatementNode(ASTNode):
    def __init__(self, variable, operator, expression):
        self.variable = variable
        self.operator = operator
        self.expression = expression

    def _extra(self):
        return f": {self.operator}"

    def children(self):
        return [self.variable, self.expression]


class DeclareStatementNode(ASTNode):
    def __init__(self, declarations):
        self.declarations = declarations or []

    def _extra(self):
        return f": {len(self.declarations)} item(s)"

    def children(self):
        return [self.declarations]


class DeclaredVariableNode(ASTNode):
    def __init__(self, name, data_type, default_value=None):
        self.name = name
        self.data_type = data_type
        self.default_value = default_value

    def _extra(self):
        display = self.name.name if hasattr(self.name, "name") else str(self.name)
        return f": {display}"

    def children(self):
        return [self.data_type, self.default_value]


class CursorDeclareNode(ASTNode):
    def __init__(self, name, select_query):
        self.name = name
        self.select_query = select_query

    def _extra(self):
        return f": {self.name.name}"

    def children(self):
        return [self.select_query]


class OpenCursorNode(ASTNode):
    def __init__(self, name):
        self.name = name

    def _extra(self):
        return f": {self.name.name}"


class FetchCursorNode(ASTNode):
    def __init__(self, name, variables=None):
        self.name = name
        self.variables = variables or []

    def _extra(self):
        return f": {self.name.name}"

    def children(self):
        return [self.variables]


class CloseCursorNode(ASTNode):
    def __init__(self, name):
        self.name = name

    def _extra(self):
        return f": {self.name.name}"


class DeallocateCursorNode(ASTNode):
    def __init__(self, name):
        self.name = name

    def _extra(self):
        return f": {self.name.name}"


class BlockNode(ASTNode):
    def __init__(self, statements):
        self.statements = statements or []

    def children(self):
        return [self.statements]


class IfStatementNode(ASTNode):
    def __init__(self, condition, then_block, else_block=None):
        self.condition = condition
        self.then_block = then_block
        self.else_block = else_block

    def children(self):
        return [self.condition, self.then_block, self.else_block]


class TryCatchNode(ASTNode):
    def __init__(self, try_block, catch_block):
        self.try_block = try_block
        self.catch_block = catch_block

    def children(self):
        return [self.try_block, self.catch_block]


class ExecuteNode(ASTNode):
    def __init__(self, target, arguments=None, output_variable=None):
        self.target = target
        self.arguments = arguments or []
        self.output_variable = output_variable

    def _extra(self):
        return f": EXEC" + (f" -> {self.output_variable.name}" if self.output_variable else "")

    def children(self):
        return [self.target, self.arguments]
