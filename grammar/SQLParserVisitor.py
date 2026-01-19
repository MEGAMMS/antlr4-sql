# Generated from grammar/SQLParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SQLParser import SQLParser
else:
    from SQLParser import SQLParser

# This class defines a complete generic visitor for a parse tree produced by SQLParser.

class SQLParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SQLParser#root.
    def visitRoot(self, ctx:SQLParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#sql_script.
    def visitSql_script(self, ctx:SQLParser.Sql_scriptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#StatementBatch.
    def visitStatementBatch(self, ctx:SQLParser.StatementBatchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#EmptyGo.
    def visitEmptyGo(self, ctx:SQLParser.EmptyGoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#sql_statement.
    def visitSql_statement(self, ctx:SQLParser.Sql_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#ddl_statement.
    def visitDdl_statement(self, ctx:SQLParser.Ddl_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#dml_statement.
    def visitDml_statement(self, ctx:SQLParser.Dml_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#create_statement.
    def visitCreate_statement(self, ctx:SQLParser.Create_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#table_element_list.
    def visitTable_element_list(self, ctx:SQLParser.Table_element_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#table_element.
    def visitTable_element(self, ctx:SQLParser.Table_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#column_def.
    def visitColumn_def(self, ctx:SQLParser.Column_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#table_constraint.
    def visitTable_constraint(self, ctx:SQLParser.Table_constraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#data_type.
    def visitData_type(self, ctx:SQLParser.Data_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#column_constraint.
    def visitColumn_constraint(self, ctx:SQLParser.Column_constraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#AlterAdd.
    def visitAlterAdd(self, ctx:SQLParser.AlterAddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#AlterDrop.
    def visitAlterDrop(self, ctx:SQLParser.AlterDropContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#AlterModify.
    def visitAlterModify(self, ctx:SQLParser.AlterModifyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#drop_statement.
    def visitDrop_statement(self, ctx:SQLParser.Drop_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#truncate_statement.
    def visitTruncate_statement(self, ctx:SQLParser.Truncate_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#use_statement.
    def visitUse_statement(self, ctx:SQLParser.Use_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#select_statement.
    def visitSelect_statement(self, ctx:SQLParser.Select_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#select_list.
    def visitSelect_list(self, ctx:SQLParser.Select_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#SelectVarAssignment.
    def visitSelectVarAssignment(self, ctx:SQLParser.SelectVarAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#SelectAliasAssignment.
    def visitSelectAliasAssignment(self, ctx:SQLParser.SelectAliasAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#SelectExpression.
    def visitSelectExpression(self, ctx:SQLParser.SelectExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#table_source.
    def visitTable_source(self, ctx:SQLParser.Table_sourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#join_part.
    def visitJoin_part(self, ctx:SQLParser.Join_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#group_list.
    def visitGroup_list(self, ctx:SQLParser.Group_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#order_list.
    def visitOrder_list(self, ctx:SQLParser.Order_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#insert_statement.
    def visitInsert_statement(self, ctx:SQLParser.Insert_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#expression_list_parens.
    def visitExpression_list_parens(self, ctx:SQLParser.Expression_list_parensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#column_list.
    def visitColumn_list(self, ctx:SQLParser.Column_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#expression_list.
    def visitExpression_list(self, ctx:SQLParser.Expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#update_statement.
    def visitUpdate_statement(self, ctx:SQLParser.Update_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#assignment_list.
    def visitAssignment_list(self, ctx:SQLParser.Assignment_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#assignment.
    def visitAssignment(self, ctx:SQLParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#delete_statement.
    def visitDelete_statement(self, ctx:SQLParser.Delete_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#declare_statement.
    def visitDeclare_statement(self, ctx:SQLParser.Declare_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#declare_list.
    def visitDeclare_list(self, ctx:SQLParser.Declare_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#declare_item.
    def visitDeclare_item(self, ctx:SQLParser.Declare_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#set_statement.
    def visitSet_statement(self, ctx:SQLParser.Set_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#control_flow_statement.
    def visitControl_flow_statement(self, ctx:SQLParser.Control_flow_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#print_statement.
    def visitPrint_statement(self, ctx:SQLParser.Print_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#execute_statement.
    def visitExecute_statement(self, ctx:SQLParser.Execute_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#with_expression.
    def visitWith_expression(self, ctx:SQLParser.With_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#LikeExpr.
    def visitLikeExpr(self, ctx:SQLParser.LikeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#IsNotNullExpr.
    def visitIsNotNullExpr(self, ctx:SQLParser.IsNotNullExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#IsNullExpr.
    def visitIsNullExpr(self, ctx:SQLParser.IsNullExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#ComparisonExpr.
    def visitComparisonExpr(self, ctx:SQLParser.ComparisonExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#BetweenExpr.
    def visitBetweenExpr(self, ctx:SQLParser.BetweenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#AtomExpr.
    def visitAtomExpr(self, ctx:SQLParser.AtomExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#UnaryExpr.
    def visitUnaryExpr(self, ctx:SQLParser.UnaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#MultiplicativeExpr.
    def visitMultiplicativeExpr(self, ctx:SQLParser.MultiplicativeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#FunctionCallExpr.
    def visitFunctionCallExpr(self, ctx:SQLParser.FunctionCallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#AdditiveExpr.
    def visitAdditiveExpr(self, ctx:SQLParser.AdditiveExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#NotExpr.
    def visitNotExpr(self, ctx:SQLParser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#InExpr.
    def visitInExpr(self, ctx:SQLParser.InExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#ParenExpr.
    def visitParenExpr(self, ctx:SQLParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#CaseExpr.
    def visitCaseExpr(self, ctx:SQLParser.CaseExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#LogicalExpr.
    def visitLogicalExpr(self, ctx:SQLParser.LogicalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#ExistsExpr.
    def visitExistsExpr(self, ctx:SQLParser.ExistsExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#ScalarSubqueryExpr.
    def visitScalarSubqueryExpr(self, ctx:SQLParser.ScalarSubqueryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#function_call.
    def visitFunction_call(self, ctx:SQLParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#atom.
    def visitAtom(self, ctx:SQLParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#table_name.
    def visitTable_name(self, ctx:SQLParser.Table_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#id_name.
    def visitId_name(self, ctx:SQLParser.Id_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#constant.
    def visitConstant(self, ctx:SQLParser.ConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#variable.
    def visitVariable(self, ctx:SQLParser.VariableContext):
        return self.visitChildren(ctx)



del SQLParser