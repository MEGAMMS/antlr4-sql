import sys
import os

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
        """استخراج النص من context"""
        if hasattr(ctx, 'getText'):
            text = ctx.getText()
            if text.startswith('[') and text.endswith(']'):
                return text[1:-1]
            elif text.startswith('"') and text.endswith('"'):
                return text[1:-1]
            return text
        return str(ctx)
    
    def _clean_identifier(self, text):
        if not text:
            return text
        
        # إزالة الأقواس المربعة
        if text.startswith('[') and text.endswith(']'):
            return text[1:-1]
        # إزالة الاقتباسات المزدوجة
        elif text.startswith('"') and text.endswith('"'):
            return text[1:-1]
        # إزالة الاقتباسات المفردة (إذا كانت مع النصوص)
        elif text.startswith("'") and text.endswith("'"):
            return text[1:-1]
        
        return text
    
    # ========== Root Rules ==========
    def visitSql_script(self, ctx):
        statements = []
        if ctx.batch():
            for batch in ctx.batch():
                batch_result = self.visit(batch)
                if batch_result:
                    if isinstance(batch_result, list):
                        statements.extend(batch_result)
                    else:
                        statements.append(batch_result)
        return statements
    
    def visitStatementBatch(self, ctx):
        statements = []
        if ctx.sql_statement():
            for stmt in ctx.sql_statement():
                result = self.visit(stmt)
                if result:
                    if isinstance(result, list):
                        statements.extend(result)
                    else:
                        statements.append(result)
        return statements
    
    def visitEmptyGo(self, ctx):
        """تجاهل عبارات GO الفارغة"""
        return None
    
    # ========== DDL Statements ==========
    def visitCreate_statement(self, ctx):
        table_name = self._clean_identifier(self._get_text(ctx.table_name()))
        
        columns = []
        constraints = []
        
        if ctx.table_element_list():
            for element in ctx.table_element_list().table_element():
                result = self.visit(element)
                if isinstance(result, ColumnDefinition):
                    columns.append(result)
                elif isinstance(result, TableConstraint):
                    constraints.append(result)
        
        return CreateTableStatement(
            table_name=table_name, 
            columns=columns, 
            constraints=constraints
        )
    
    def visitColumn_def(self, ctx):
        col_name = self._clean_identifier(self._get_text(ctx.id_name()))
        
        data_type = None
        if ctx.data_type():
            data_type = self.visit(ctx.data_type())
        
        constraints = []
        if ctx.column_constraint():
            for constr in ctx.column_constraint():
                constraint = self.visit(constr)
                if constraint:
                    constraints.append(constraint)
        
        return ColumnDefinition(
            name=col_name, 
            data_type=data_type, 
            constraints=constraints
        )
    
    def visitData_type(self, ctx):
        type_name = self._get_text(ctx.id_name(0))
        params = []
        
        if ctx.LPAREN():
            if ctx.INT():
                int_tokens = ctx.INT()
                for i, int_token in enumerate(int_tokens):
                    try:
                        params.append(int(int_token.getText()))
                    except:
                        params.append(int_token.getText())
            elif len(ctx.id_name()) > 1:
                for i in range(1, len(ctx.id_name())):
                    param_name = self._get_text(ctx.id_name(i))
                    params.append(param_name)
        
        return DataType(name=type_name, params=params)
    
    def visitColumn_constraint(self, ctx):
        if ctx.NOT() and ctx.NULL():
            return ColumnConstraint(type='NOT_NULL')
        elif ctx.NULL():
            return ColumnConstraint(type='NULL')
        elif ctx.PRIMARY() and ctx.KEY():
            return ColumnConstraint(type='PRIMARY_KEY')
        elif ctx.UNIQUE():
            return ColumnConstraint(type='UNIQUE')
        elif ctx.DEFAULT():
            expr = self.visit(ctx.expression()) if ctx.expression() else None
            return ColumnConstraint(type='DEFAULT', value=expr)
        elif ctx.IDENTITY():
            return ColumnConstraint(type='IDENTITY')
        elif ctx.REFERENCES():
            table_name = self._clean_identifier(self._get_text(ctx.table_name()))
            col_name = self._clean_identifier(self._get_text(ctx.id_name()))
            return ColumnConstraint(type='REFERENCES', value=ColumnReference(name=col_name, table=table_name))
        
        return None
    
    def visitTable_constraint(self, ctx):
        """معالجة قيود الجداول"""
        if ctx.PRIMARY() and ctx.KEY():
            columns = [self._clean_identifier(self._get_text(col)) 
                      for col in ctx.column_list().id_name()]
            name = self._clean_identifier(self._get_text(ctx.id_name(0))) if ctx.id_name() else None
            return TableConstraint(type='PRIMARY_KEY', columns=columns, name=name)
        elif ctx.FOREIGN() and ctx.KEY():
            columns = [self._clean_identifier(self._get_text(col)) 
                      for col in ctx.column_list(0).id_name()]
            ref_table = self._clean_identifier(self._get_text(ctx.table_name()))
            ref_columns = [self._clean_identifier(self._get_text(col)) 
                          for col in ctx.column_list(1).id_name()]
            name = self._clean_identifier(self._get_text(ctx.id_name(0))) if ctx.id_name() else None
            return TableConstraint(
                type='FOREIGN_KEY', 
                columns=columns, 
                name=name,
                ref_table=ref_table,
                ref_columns=ref_columns
            )
        
        return None
    
    # ========== DML Statements ==========
    def visitSelect_statement(self, ctx):
        # SELECT List
        select_items = []
        if ctx.select_list():
            select_items_result = self.visit(ctx.select_list())
            if isinstance(select_items_result, list):
                select_items = select_items_result
            elif select_items_result:
                select_items = [select_items_result]
        
        # FROM Clause
        from_clause = None
        if ctx.table_source():
            from_clause = self.visit(ctx.table_source())
        
        # WHERE Clause
        where_clause = None
        if ctx.expression():
            where_clause = self.visit(ctx.expression(0))
        
        # GROUP BY
        group_by = []
        if ctx.group_list():
            group_result = self.visit(ctx.group_list())
            if isinstance(group_result, list):
                group_by = group_result
            elif group_result:
                group_by = [group_result]
        
        # HAVING
        having_clause = None
        if ctx.expression():
            for i in range(ctx.getChildCount()):
                child = ctx.getChild(i)
                if isinstance(child, TerminalNodeImpl) and child.getText().upper() == 'HAVING':
                    if i + 1 < ctx.getChildCount():
                        having_clause = self.visit(ctx.expression(1))
                    break
        
        # ORDER BY
        order_by = []
        if ctx.order_list():
            order_result = self.visit(ctx.order_list())
            if isinstance(order_result, list):
                order_by = order_result
            elif order_result:
                order_by = [order_result]
        
        # JOINs
        joins = []
        if ctx.join_part():
            for join in ctx.join_part():
                join_result = self.visit(join)
                if join_result:
                    joins.append(join_result)
        
        # Flags
        distinct = bool(ctx.DISTINCT())
        top = int(ctx.INT().getText()) if ctx.TOP() and ctx.INT() else None
        
        # بناء كائن SelectStatement
        stmt = SelectStatement(
            select_list=select_items,
            from_clause=from_clause,
            where_clause=where_clause,
            group_by=group_by,
            having_clause=having_clause,
            order_by=order_by,
            distinct=distinct,
            top=top
        )
        
        # إضافة الـ joins كخاصية إضافية
        if joins:
            stmt.joins = joins
        
        return stmt
    
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
        alias = None
        
        if ctx.id_name():
            alias_text = self._get_text(ctx.id_name())
            # تنظيف الاسم إذا كان بين اقتباسات
            alias = self._clean_identifier(alias_text)
            # إذا كان الاسم بين اقتباسات مفردة (كلمة محجوزة)
            if alias.startswith("'") and alias.endswith("'"):
                alias = alias[1:-1]
        
        return SelectItem(expression=expr, alias=alias)
    
    def visitTable_source(self, ctx):
        source = None
        alias = None
        
        if ctx.table_name():
            source_text = self._get_text(ctx.table_name())
            source = self._clean_identifier(source_text)
        elif ctx.select_statement():
            source = self.visit(ctx.select_statement())
        
        if ctx.id_name():
            alias_text = self._get_text(ctx.id_name())
            alias = self._clean_identifier(alias_text)
        
        return TableSource(source=source, alias=alias)
    
    def visitJoin_part(self, ctx):
        """معالجة JOINs"""
        join_type = 'INNER'  # الافتراضي
        
        if ctx.INNER():
            join_type = 'INNER'
        elif ctx.LEFT():
            join_type = 'LEFT'
        elif ctx.RIGHT():
            join_type = 'RIGHT'
        elif ctx.FULL():
            join_type = 'FULL'
        elif ctx.CROSS():
            join_type = 'CROSS'
        
        table_source = self.visit(ctx.table_source()) if ctx.table_source() else None
        condition = self.visit(ctx.expression()) if ctx.expression() else None
        
        # إرجاع كائن بسيط للـ JOIN
        return {
            'type': join_type,
            'table': table_source,
            'condition': condition
        }
    
    def visitOrder_list(self, ctx):
        items = []
        expressions = ctx.expression()
        
        for i, expr_ctx in enumerate(expressions):
            direction = 'ASC'
            
            # البحث عن ASC/DESC بعد التعبير
            if i < len(expressions) - 1:
                next_child = ctx.getChild(ctx.children.index(expr_ctx) + 1)
                if isinstance(next_child, TerminalNodeImpl):
                    if next_child.getText().upper() == 'ASC':
                        direction = 'ASC'
                    elif next_child.getText().upper() == 'DESC':
                        direction = 'DESC'
            
            expr = self.visit(expr_ctx)
            if expr:
                items.append(OrderByItem(expression=expr, direction=direction))
        
        return items
    
    def visitGroup_list(self, ctx):
        expressions = []
        if ctx.expression():
            for expr in ctx.expression():
                result = self.visit(expr)
                if result:
                    expressions.append(result)
        return expressions
    
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
    
    def visitLogicalExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.getChild(1).getText().upper()  # AND أو OR
        return BinaryExpression(left=left, operator=op, right=right)
    
    def visitLikeExpr(self, ctx):
        value = self.visit(ctx.expression(0))
        pattern = self.visit(ctx.expression(1))
        not_like = bool(ctx.NOT())
        return LikeExpression(value=value, pattern=pattern, not_like=not_like)
    
    def visitBetweenExpr(self, ctx):
        value = self.visit(ctx.expression(0))
        lower = self.visit(ctx.expression(1))
        upper = self.visit(ctx.expression(2))
        not_between = bool(ctx.NOT())
        return BetweenExpression(
            value=value, 
            lower=lower, 
            upper=upper, 
            not_between=not_between
        )
    
    def visitInExpr(self, ctx):
        value = self.visit(ctx.expression(0))
        not_in = bool(ctx.NOT())
        
        items = None
        if ctx.expression_list():
            items = self.visit(ctx.expression_list())
        elif ctx.select_statement():
            items = self.visit(ctx.select_statement())
        
        return InExpression(value=value, items=items, not_in=not_in)
    
    def visitIsNullExpr(self, ctx):
        value = self.visit(ctx.expression(0))
        return IsNullExpression(value=value, not_null=False)
    
    def visitIsNotNullExpr(self, ctx):
        value = self.visit(ctx.expression(0))
        return IsNullExpression(value=value, not_null=True)
    
    def visitUnaryExpr(self, ctx):
        operand = self.visit(ctx.expression(0))
        op = ctx.getChild(0).getText()  # + أو -
        return UnaryExpression(operator=op, operand=operand)
    
    def visitNotExpr(self, ctx):
        operand = self.visit(ctx.expression(0))
        return UnaryExpression(operator='NOT', operand=operand)
    
    def visitParenExpr(self, ctx):
        return self.visit(ctx.expression(0))
    
    def visitAtomExpr(self, ctx):
        return self.visit(ctx.atom())
    
    def visitAtom(self, ctx):
        if ctx.table_name():
            table_parts = ctx.table_name().getText().split('.')
            if len(table_parts) == 2:
                return ColumnReference(name=self._clean_identifier(table_parts[1]), 
                                      table=self._clean_identifier(table_parts[0]))
            else:
                return ColumnReference(name=self._clean_identifier(ctx.table_name().getText()))
        elif ctx.constant():
            return self.visit(ctx.constant())
        elif ctx.variable():
            var_name = self._get_text(ctx.variable())
            return VariableReference(name=var_name)
        return None
    
    def visitConstant(self, ctx):
        if ctx.INT():
            try:
                return Literal(value=int(ctx.INT().getText()), type='INT')
            except:
                return Literal(value=ctx.INT().getText(), type='INT')
        elif ctx.FLOAT():
            try:
                return Literal(value=float(ctx.FLOAT().getText()), type='FLOAT')
            except:
                return Literal(value=ctx.FLOAT().getText(), type='FLOAT')
        elif ctx.STRING():
            text = ctx.STRING().getText()
            # إزالة الاقتباسات الخارجية
            if len(text) >= 2 and text[0] == "'" and text[-1] == "'":
                text = text[1:-1]
                # معالجة الاقتباسات المزدوجة داخل النص
                text = text.replace("''", "'")
            return Literal(value=text, type='STRING')
        elif ctx.NSTRING():
            text = ctx.NSTRING().getText()
            if len(text) >= 3 and text[0] in ('n', 'N') and text[1] == "'" and text[-1] == "'":
                text = text[2:-1]
                text = text.replace("''", "'")
            return Literal(value=text, type='NSTRING')
        elif ctx.NULL():
            return Literal(value=None, type='NULL')
        elif ctx.TRUE():
            return Literal(value=True, type='BOOLEAN')
        elif ctx.FALSE():
            return Literal(value=False, type='BOOLEAN')
        return None
    
    def visitExpression_list(self, ctx):
        expressions = []
        if ctx.expression():
            for expr in ctx.expression():
                result = self.visit(expr)
                if result:
                    expressions.append(result)
        return expressions
    
    def visitFunction_call(self, ctx):
        func_name = self._clean_identifier(self._get_text(ctx.id_name()))
        arguments = []
        
        if ctx.expression_list():
            arguments = self.visit(ctx.expression_list())
        
        return FunctionCall(name=func_name, arguments=arguments)
    
    # ========== Other Statements ==========
    def visitInsert_statement(self, ctx):
        table_name = self._clean_identifier(self._get_text(ctx.table_name()))
        
        columns = None
        if ctx.column_list():
            columns = [self._clean_identifier(self._get_text(col)) 
                      for col in ctx.column_list().id_name()]
        
        if ctx.VALUES():
            values = []
            for expr_list_ctx in ctx.expression_list_parens():
                if expr_list_ctx.expression_list():
                    values.append(self.visit(expr_list_ctx.expression_list()))
            return InsertStatement(table_name=table_name, columns=columns, values=values)
        elif ctx.select_statement():
            select_query = self.visit(ctx.select_statement())
            return InsertStatement(table_name=table_name, columns=columns, 
                                 select_query=select_query)
        
        return None
    
    def visitUpdate_statement(self, ctx):
        table_name = self._clean_identifier(self._get_text(ctx.table_name()))
        assignments = []
        
        if ctx.assignment_list():
            assignments_result = self.visit(ctx.assignment_list())
            if isinstance(assignments_result, list):
                assignments = assignments_result
            elif assignments_result:
                assignments = [assignments_result]
        
        where_clause = self.visit(ctx.expression()) if ctx.expression() else None
        
        return UpdateStatement(
            table_name=table_name, 
            assignments=assignments, 
            where_clause=where_clause
        )
    
    def visitAssignment_list(self, ctx):
        assignments = []
        if ctx.assignment():
            for assign in ctx.assignment():
                result = self.visit(assign)
                if result:
                    assignments.append(result)
        return assignments
    
    def visitAssignment(self, ctx):
        column = self._clean_identifier(self._get_text(ctx.id_name(0)))
        operator = ctx.getChild(1).getText()
        value = self.visit(ctx.expression())
        return Assignment(column=column, operator=operator, value=value)
    
    def visitDelete_statement(self, ctx):
        table_name = self._clean_identifier(self._get_text(ctx.table_name()))
        where_clause = self.visit(ctx.expression()) if ctx.expression() else None
        return DeleteStatement(table_name=table_name, where_clause=where_clause)
    
    def visitUse_statement(self, ctx):
        database = self._clean_identifier(self._get_text(ctx.id_name()))
        return UseStatement(database=database)
    
    def visitPrint_statement(self, ctx):
        expr = self.visit(ctx.expression())
        return PrintStatement(expression=expr)
    
    def visitDeclare_statement(self, ctx):
        variables = []
        if ctx.declare_list():
            vars_result = self.visit(ctx.declare_list())
            if isinstance(vars_result, list):
                variables = vars_result
            elif vars_result:
                variables = [vars_result]
        return DeclareStatement(variables=variables)
    
    def visitDeclare_list(self, ctx):
        variables = []
        if ctx.declare_item():
            for item in ctx.declare_item():
                result = self.visit(item)
                if result:
                    variables.append(result)
        return variables
    
    def visitDeclare_item(self, ctx):
        var_name = self._get_text(ctx.LOCAL_VAR())
        data_type = None
        initial_value = None
        
        if ctx.data_type():
            data_type = self.visit(ctx.data_type())
        if ctx.expression():
            initial_value = self.visit(ctx.expression())
        
        return VariableDeclaration(
            name=var_name, 
            data_type=data_type, 
            initial_value=initial_value
        )
    
    def visitSet_statement(self, ctx):
        variable = self._get_text(ctx.variable())
        operator = ctx.getChild(1).getText()
        value = self.visit(ctx.expression())
        return SetStatement(variable=variable, operator=operator, value=value)
    
    def visitControl_flow_statement(self, ctx):
        return None
    
    def visitIf_statement(self, ctx):
        condition = self.visit(ctx.expression()) if ctx.expression() else None
        then_stmt = self.visit(ctx.sql_statement(0)) if ctx.sql_statement() and len(ctx.sql_statement()) > 0 else None
        else_stmt = self.visit(ctx.sql_statement(1)) if ctx.ELSE() and ctx.sql_statement() and len(ctx.sql_statement()) > 1 else None
        
        then_branch = [then_stmt] if then_stmt else []
        else_branch = [else_stmt] if else_stmt else []
        
        return IfStatement(condition=condition, then_branch=then_branch, else_branch=else_branch)
    
    def visitExecute_statement(self, ctx):
        return None
    
    def visitWith_expression(self, ctx):
        return None
    
    # ========== Default Visit Methods ==========
    def defaultResult(self):
        return None
    
    def aggregateResult(self, aggregate, nextResult):
        if aggregate is None:
            return nextResult
        if nextResult is None:
            return aggregate
        
        if isinstance(aggregate, list):
            if isinstance(nextResult, list):
                aggregate.extend(nextResult)
            else:
                aggregate.append(nextResult)
            return aggregate
        elif isinstance(nextResult, list):
            return [aggregate] + nextResult
        else:
            return [aggregate, nextResult]