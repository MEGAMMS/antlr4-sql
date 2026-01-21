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
