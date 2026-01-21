from antlr4 import *
from src.antlr_generated.SQLParserVisitor import SQLParserVisitor
from src.antlr_generated.SQLParser import SQLParser

from .ast_nodes import (
    ProgramNode,
    SelectNode,
    IdentifierNode,
    LiteralNode,
    BinaryExpressionNode,
    UnaryExpressionNode,
    OrderByNode
)

class ASTBuilder(SQLParserVisitor):

    def visitRoot(self, ctx):
        statements = self.visit(ctx.sql_script())
        return ProgramNode(statements)
    
    def visitSql_script(self, ctx):
        statements = []
        for batch in ctx.batch():
            result = self.visit(batch)
            if isinstance(result, list):
                statements.extend(result)
            elif result:
                statements.append(result)
        return statements
    
    def visitStatementBatch(self, ctx):
        statements = []
        for stmt in ctx.sql_statement():
            node = self.visit(stmt)
            if node:
                statements.append(node)
        return statements

    def visitSql_statement(self, ctx):
        if ctx.select_statement():
            return self.visit(ctx.select_statement())
        return None

    def visitSelect_statement(self, ctx):
        columns = self.visit(ctx.select_list())
        table = self.visit(ctx.table_source())

        where = None
        if ctx.expression():
            where = self.visit(ctx.expression(0))

        order_by = []
        if ctx.order_list():
            order_by = self.visit(ctx.order_list())

        return SelectNode(
            columns=columns,
            table=table,
            where=where,
            order_by=order_by
        )

    def visitSelect_list(self, ctx):
        if ctx.STAR():
            return [IdentifierNode("*")]

        items = []
        for item in ctx.select_item():
            items.append(self.visit(item))
        return items
    
    def visitSelectExpression(self, ctx):
        expr = self.visit(ctx.expression())

        if ctx.id_name():
            alias = ctx.id_name().getText()
            return IdentifierNode(f"{expr.name} AS {alias}")

        return expr
    

    def visitTable_source(self, ctx):
        name = ctx.table_name().getText()
        return IdentifierNode(name)

    def visitAdditiveExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.getChild(1).getText()
        return BinaryExpressionNode(op, left, right)

    def visitMultiplicativeExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.getChild(1).getText()
        return BinaryExpressionNode(op, left, right)

    def visitComparisonExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.getChild(1).getText()
        return BinaryExpressionNode(op, left, right)

    def visitUnaryExpr(self, ctx):
        expr = self.visit(ctx.expression(0))
        op = ctx.getChild(0).getText()
        return UnaryExpressionNode(op, expr)
