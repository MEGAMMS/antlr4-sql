import sys
import os

# إضافة المسار للوصول إلى antlr_generated
sys.path.append(os.path.join(os.path.dirname(__file__), '../../src/antlr_generated'))

from antlr4 import *
from src.antlr_generated.SQLParserVisitor import SQLParserVisitor
from src.antlr_generated.SQLParser import SQLParser

from .ast_nodes import *

class ASTBuilder(SQLParserVisitor):
    
    def __init__(self):
        super().__init__()
    
    # ========== Helper Methods ==========
    def _get_text(self, ctx):
        if hasattr(ctx, 'getText'):
            return ctx.getText()
        return str(ctx)
    
    def _visit_children(self, ctx):
        """زيارة جميع الأطفال"""
        results = []
        if hasattr(ctx, 'children') and ctx.children:
            for child in ctx.children:
                result = self.visit(child)
                if result:
                    results.append(result)
        return results
    
    # ========== Root Rules ==========
    def visitSql_script(self, ctx):
        statements = []
        if ctx.batch():
            for batch in ctx.batch():
                batch_statements = self.visit(batch)
                if isinstance(batch_statements, list):
                    statements.extend(batch_statements)
                elif batch_statements:
                    statements.append(batch_statements)
        return statements
    
    def visitStatementBatch(self, ctx):
        statements = []
        for stmt in ctx.sql_statement():
            result = self.visit(stmt)
            if result:
                statements.append(result)
        return statements
    
    # ========== DDL Statements ==========
    def visitCreate_statement(self, ctx):
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
        
        return CreateTableStatement(table_name=table_name, columns=columns, constraints=constraints)
    
    def visitColumn_def(self, ctx):
        col_name = self._get_text(ctx.id_name())
        
        data_type = None
        if ctx.data_type():
            data_type = self.visit(ctx.data_type())
        
        constraints = []
        if ctx.column_constraint():
            for constr in ctx.column_constraint():
                constraint = self.visit(constr)
                if constraint:
                    constraints.append(constraint)
        
        return ColumnDefinition(name=col_name, data_type=data_type, constraints=constraints)
    
    def visitData_type(self, ctx):
        type_name = self._get_text(ctx.id_name())
        params = []
        
        if ctx.INT():
            params.append(int(ctx.INT().getText()))
            if ctx.COMMA() and len(ctx.INT()) > 1:
                params.append(int(ctx.INT(1).getText()))
        
        return DataType(name=type_name, params=params)
    
    # ========== DML Statements ==========
    def visitSelect_statement(self, ctx):
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
            where_clause = self.visit(ctx.expression(0))
        
        # ORDER BY
        order_by = []
        if ctx.order_list():
            order_by = self.visit(ctx.order_list())
        
        # Flags
        distinct = bool(ctx.DISTINCT())
        top = int(ctx.INT().getText()) if ctx.TOP() and ctx.INT() else None
        
        return SelectStatement(
            select_list=select_items,
            from_clause=from_clause,
            where_clause=where_clause,
            order_by=order_by,
            distinct=distinct,
            top=top
        )
    
    def visitSelect_list(self, ctx):
        items = []
        if ctx.STAR():
            items.append(SelectItem(expression=ColumnReference("*")))
        elif ctx.select_item():
            for item in ctx.select_item():
                result = self.visit(item)
                if result:
                    items.append(result)
        return items
    
    def visitSelectExpression(self, ctx):
        expr = self.visit(ctx.expression())
        alias = self._get_text(ctx.id_name()) if ctx.id_name() else None
        return SelectItem(expression=expr, alias=alias)
    
    def visitTable_source(self, ctx):
        if ctx.table_name():
            source = self._get_text(ctx.table_name())
        elif ctx.select_statement():
            source = self.visit(ctx.select_statement())
        else:
            source = None
        
        alias = self._get_text(ctx.id_name()) if ctx.id_name() else None
        return TableSource(source=source, alias=alias)
    
    def visitOrder_list(self, ctx):
        items = []
        expressions = ctx.expression()
        directions = []
        
        # جمع الاتجاهات
        for i in range(len(expressions)):
            direction = 'ASC'
            items.append(OrderByItem(
                expression=self.visit(expressions[i]),
                direction=direction
            ))
        
        return items
    
    # ========== Expressions ==========
    def visitComparisonExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.getChild(1).getText()
        return BinaryExpression(left=left, operator=op, right=right)
    
    def visitAdditiveExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.getChild(1).getText()
        return BinaryExpression(left=left, operator=op, right=right)
    
    def visitMultiplicativeExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.getChild(1).getText()
        return BinaryExpression(left=left, operator=op, right=right)
    
    def visitAtomExpr(self, ctx):
        return self.visit(ctx.atom())
    
    def visitAtom(self, ctx):
        if ctx.table_name():
            return ColumnReference(name=self._get_text(ctx.table_name()))
        elif ctx.constant():
            return self.visit(ctx.constant())
        elif ctx.variable():
            return VariableReference(name=self._get_text(ctx.variable()))
        return None
    
    def visitConstant(self, ctx):
        if ctx.INT():
            return Literal(value=int(ctx.INT().getText()), type='INT')
        elif ctx.FLOAT():
            return Literal(value=float(ctx.FLOAT().getText()), type='FLOAT')
        elif ctx.STRING():
            text = ctx.STRING().getText()[1:-1]  # إزالة الاقتباسات
            return Literal(value=text, type='STRING')
        elif ctx.NULL():
            return Literal(value=None, type='NULL')
        return None
    
    # ========== Other Statements ==========
    def visitInsert_statement(self, ctx):
        table_name = self._get_text(ctx.table_name())
        
        columns = None
        if ctx.column_list():
            columns = [self._get_text(col) for col in ctx.column_list().id_name()]
        
        if ctx.VALUES():
            values = []
            for expr_list in ctx.expression_list_parens():
                values.append(self.visit(expr_list.expression_list()))
            return InsertStatement(table_name=table_name, columns=columns, values=values)
        
        return None
    
    def visitUpdate_statement(self, ctx):
        table_name = self._get_text(ctx.table_name())
        assignments = self.visit(ctx.assignment_list())
        where_clause = self.visit(ctx.expression()) if ctx.expression() else None
        return UpdateStatement(table_name=table_name, assignments=assignments, where_clause=where_clause)
    
    def visitDelete_statement(self, ctx):
        table_name = self._get_text(ctx.table_name())
        where_clause = self.visit(ctx.expression()) if ctx.expression() else None
        return DeleteStatement(table_name=table_name, where_clause=where_clause)
    
    def visitUse_statement(self, ctx):
        database = self._get_text(ctx.id_name())
        return UseStatement(database=database)
    
    def visitPrint_statement(self, ctx):
        expr = self.visit(ctx.expression())
        return PrintStatement(expression=expr)
    
    def visitDeclare_statement(self, ctx):
        variables = self.visit(ctx.declare_list())
        return DeclareStatement(variables=variables)
    
    def visitSet_statement(self, ctx):
        variable = self._get_text(ctx.variable())
        operator = ctx.getChild(1).getText()
        value = self.visit(ctx.expression())
        return SetStatement(variable=variable, operator=operator, value=value)
    
    # ========== Default Visit ==========
    def defaultResult(self):
        return None