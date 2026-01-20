# ast_builder.py

from antlr4 import ParseTreeVisitor
from antlr4.tree.Tree import TerminalNodeImpl

from src.antlr_generated.SQLParser import SQLParser
from ast_nodes import *

class ASTBuilder(ParseTreeVisitor):
    
    def __init__(self):
        super().__init__()
    
    # ========== Visit Methods ==========
    
    def visitSql_script(self, ctx: SQLParser.Sql_scriptContext):
        statements = []
        if ctx.batch():
            for batch in ctx.batch():
                batch_statements = self.visit(batch)
                if isinstance(batch_statements, list):
                    statements.extend(batch_statements)
                elif batch_statements:
                    statements.append(batch_statements)
        return statements
    
    def visitStatementBatch(self, ctx: SQLParser.StatementBatchContext):
        statements = []
        for stmt in ctx.sql_statement():
            result = self.visit(stmt)
            if result:
                statements.append(result)
        return statements
    
    def visitCreate_statement(self, ctx: SQLParser.Create_statementContext):
        table_name = self._get_text(ctx.table_name())
        
        columns = []
        constraints = []
        
        if ctx.table_element_list():
            for element in ctx.table_element_list().table_element():
                result = self.visit(element)
                if isinstance(result, ColumnDefinition):
                    columns.append(result)
                elif isinstance(result, TableConstraint):
                    constraints.append(result)
        
        return CreateTableStatement(table_name, columns, constraints)
    
    def visitColumn_def(self, ctx: SQLParser.Column_defContext):
        col_name = self._get_text(ctx.id_name())
        data_type = self.visit(ctx.data_type()) if ctx.data_type() else None
        
        constraints = []
        if ctx.column_constraint():
            for constr_ctx in ctx.column_constraint():
                constraint = self.visit(constr_ctx)
                if constraint:
                    constraints.append(constraint)
        
        return ColumnDefinition(col_name, data_type, constraints)
    
    def visitData_type(self, ctx: SQLParser.Data_typeContext):
        type_name = self._get_text(ctx.id_name())
        params = []
        
        if ctx.INT():
            params = [int(ctx.INT(0).getText())]
            if ctx.COMMA() and ctx.INT(1):
                params.append(int(ctx.INT(1).getText()))
        
        return DataType(type_name, params)
    
    def visitSelect_statement(self, ctx: SQLParser.Select_statementContext):
        # SELECT List
        select_items = []
        if ctx.select_list():
            select_items = self.visit(ctx.select_list())
        
        # FROM Clause
        from_clause = None
        if ctx.table_source():
            from_clause = self.visit(ctx.table_source())
        
        # WHERE Clause
        where_clause = None
        if ctx.expression():
            where_clause = self.visit(ctx.expression())
        
        # GROUP BY
        group_by = []
        if ctx.group_list():
            group_by = self.visit(ctx.group_list())
        
        # HAVING
        having_clause = None
        if ctx.expression():
            having_clause = self.visit(ctx.expression())
        
        # ORDER BY
        order_by = []
        if ctx.order_list():
            order_by = self.visit(ctx.order_list())
        
        # Flags
        distinct = bool(ctx.DISTINCT())
        top = int(ctx.INT().getText()) if ctx.TOP() and ctx.INT() else None
        
        return SelectStatement(
            select_items, from_clause, where_clause,
            group_by, having_clause, order_by,
            distinct, top
        )
    
    def visitSelect_list(self, ctx: SQLParser.Select_listContext):
        items = []
        if ctx.STAR():
            items.append(SelectItem(ColumnReference("*")))
        elif ctx.select_item():
            for item_ctx in ctx.select_item():
                result = self.visit(item_ctx)
                if result:
                    items.append(result)
        return items
    
    def visitSelectExpression(self, ctx: SQLParser.SelectExpressionContext):
        expr = self.visit(ctx.expression())
        alias = self._get_text(ctx.id_name()) if ctx.id_name() else None
        return SelectItem(expr, alias)
    
    def visitExpression(self, ctx: SQLParser.ExpressionContext):
        # Binary Operators
        if ctx.getChildCount() == 3 and ctx.getChild(1) not in [TerminalNodeImpl]:
            left = self.visit(ctx.expression(0))
            right = self.visit(ctx.expression(1))
            op = self._get_text(ctx.getChild(1))
            
            if ctx.STAR() or ctx.SLASH() or ctx.PERCENT():
                return BinaryExpression(left, op, right)
            elif ctx.PLUS() or ctx.MINUS():
                return BinaryExpression(left, op, right)
            elif ctx.EQ() or ctx.NEQ() or ctx.GT() or ctx.LT() or ctx.GE() or ctx.LE():
                return BinaryExpression(left, op, right)
            elif ctx.AND() or ctx.OR():
                return BinaryExpression(left, op, right)
        
        # Unary Operators
        elif ctx.getChildCount() == 2:
            if ctx.PLUS() or ctx.MINUS():
                return UnaryExpression(self._get_text(ctx.getChild(0)), self.visit(ctx.expression(0)))
            elif ctx.NOT():
                return UnaryExpression('NOT', self.visit(ctx.expression(0)))
        
        # Parentheses
        elif ctx.LPAREN() and ctx.RPAREN():
            return self.visit(ctx.expression(0))
        
        # Function Call
        elif ctx.function_call():
            return self.visit(ctx.function_call())
        
        # Atom
        elif ctx.atom():
            return self.visit(ctx.atom())
        
        # TODO: Handle other expression types
        
        return None
    
    def visitAtom(self, ctx: SQLParser.AtomContext):
        if ctx.INT():
            return Literal(int(ctx.INT().getText()), 'INT')
        elif ctx.FLOAT():
            return Literal(float(ctx.FLOAT().getText()), 'FLOAT')
        elif ctx.STRING():
            text = ctx.STRING().getText()[1:-1]  # Remove quotes
            return Literal(text, 'STRING')
        elif ctx.NULL():
            return Literal(None, 'NULL')
        elif ctx.TRUE():
            return Literal(True, 'BOOLEAN')
        elif ctx.FALSE():
            return Literal(False, 'BOOLEAN')
        elif ctx.variable():
            return VariableReference(self._get_text(ctx.variable()))
        elif ctx.table_name():
            return ColumnReference(self._get_text(ctx.table_name()))
        
        return None
    
    def visitFunction_call(self, ctx: SQLParser.Function_callContext):
        func_name = self._get_text(ctx.id_name())
        args = []
        
        if ctx.expression_list():
            args = self.visit(ctx.expression_list())
        
        return FunctionCall(func_name, args)
    
    def visitExpression_list(self, ctx: SQLParser.Expression_listContext):
        return [self.visit(expr) for expr in ctx.expression()]
    
    def visitInsert_statement(self, ctx: SQLParser.Insert_statementContext):
        table_name = self._get_text(ctx.table_name())
        columns = None
        
        if ctx.column_list():
            columns = [self._get_text(col) for col in ctx.column_list().id_name()]
        
        if ctx.VALUES():
            values = []
            for expr_list in ctx.expression_list_parens():
                values.append(self.visit(expr_list.expression_list()))
            return InsertStatement(table_name, columns, values)
        elif ctx.select_statement():
            select_query = self.visit(ctx.select_statement())
            return InsertStatement(table_name, columns, None, select_query)
        
        return None
    
    def visitUpdate_statement(self, ctx: SQLParser.Update_statementContext):
        table_name = self._get_text(ctx.table_name())
        assignments = self.visit(ctx.assignment_list())
        where_clause = self.visit(ctx.expression()) if ctx.expression() else None
        
        return UpdateStatement(table_name, assignments, where_clause)
    
    def visitAssignment_list(self, ctx: SQLParser.Assignment_listContext):
        return [self.visit(assignment) for assignment in ctx.assignment()]
    
    def visitAssignment(self, ctx: SQLParser.AssignmentContext):
        column = self._get_text(ctx.id_name(0))
        operator = self._get_text(ctx.getChild(1))
        value = self.visit(ctx.expression())
        
        return Assignment(column, operator, value)
    
    def visitDelete_statement(self, ctx: SQLParser.Delete_statementContext):
        table_name = self._get_text(ctx.table_name())
        where_clause = self.visit(ctx.expression()) if ctx.expression() else None
        
        return DeleteStatement(table_name, where_clause)
    
    def visitDeclare_statement(self, ctx: SQLParser.Declare_statementContext):
        variables = self.visit(ctx.declare_list())
        return DeclareStatement(variables)
    
    def visitDeclare_list(self, ctx: SQLParser.Declare_listContext):
        return [self.visit(item) for item in ctx.declare_item()]
    
    def visitDeclare_item(self, ctx: SQLParser.Declare_itemContext):
        var_name = self._get_text(ctx.LOCAL_VAR())
        data_type = self.visit(ctx.data_type()) if ctx.data_type() else None
        initial_value = self.visit(ctx.expression()) if ctx.expression() else None
        
        return VariableDeclaration(var_name, data_type, initial_value)
    
    def visitSet_statement(self, ctx: SQLParser.Set_statementContext):
        variable = self._get_text(ctx.variable())
        operator = self._get_text(ctx.getChild(1))  # EQ, PLUS_ASSIGN, etc.
        value = self.visit(ctx.expression())
        
        return SetStatement(variable, operator, value)
    
    def visitUse_statement(self, ctx: SQLParser.Use_statementContext):
        database = self._get_text(ctx.id_name())
        return UseStatement(database)
    
    def visitPrint_statement(self, ctx: SQLParser.Print_statementContext):
        expr = self.visit(ctx.expression())
        return PrintStatement(expr)
    
    def visitIf_statement(self, ctx: SQLParser.If_statementContext):
        condition = self.visit(ctx.expression())
        then_stmt = self.visit(ctx.sql_statement(0))
        else_stmt = self.visit(ctx.sql_statement(1)) if ctx.ELSE() else None
        
        then_branch = [then_stmt] if then_stmt else []
        else_branch = [else_stmt] if else_stmt else []
        
        return IfStatement(condition, then_branch, else_branch)
    
    # ========== Helper Methods ==========
    
    def _get_text(self, ctx):
        if hasattr(ctx, 'getText'):
            return ctx.getText()
        return str(ctx)
    
    def visit_generic(self, node):
        if hasattr(node, 'children') and node.children:
            results = []
            for child in node.children:
                result = self.visit(child)
                if result:
                    results.append(result)
            return results if len(results) > 1 else (results[0] if results else None)
        return None
    
    def visitTerminal(self, node):
        return None