# Generated from grammar/SQLParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SQLParser import SQLParser
else:
    from SQLParser import SQLParser

# This class defines a complete listener for a parse tree produced by SQLParser.
class SQLParserListener(ParseTreeListener):

    # Enter a parse tree produced by SQLParser#root.
    def enterRoot(self, ctx:SQLParser.RootContext):
        pass

    # Exit a parse tree produced by SQLParser#root.
    def exitRoot(self, ctx:SQLParser.RootContext):
        pass


    # Enter a parse tree produced by SQLParser#sql_script.
    def enterSql_script(self, ctx:SQLParser.Sql_scriptContext):
        pass

    # Exit a parse tree produced by SQLParser#sql_script.
    def exitSql_script(self, ctx:SQLParser.Sql_scriptContext):
        pass


    # Enter a parse tree produced by SQLParser#StatementBatch.
    def enterStatementBatch(self, ctx:SQLParser.StatementBatchContext):
        pass

    # Exit a parse tree produced by SQLParser#StatementBatch.
    def exitStatementBatch(self, ctx:SQLParser.StatementBatchContext):
        pass


    # Enter a parse tree produced by SQLParser#EmptyGo.
    def enterEmptyGo(self, ctx:SQLParser.EmptyGoContext):
        pass

    # Exit a parse tree produced by SQLParser#EmptyGo.
    def exitEmptyGo(self, ctx:SQLParser.EmptyGoContext):
        pass


    # Enter a parse tree produced by SQLParser#sql_statement.
    def enterSql_statement(self, ctx:SQLParser.Sql_statementContext):
        pass

    # Exit a parse tree produced by SQLParser#sql_statement.
    def exitSql_statement(self, ctx:SQLParser.Sql_statementContext):
        pass


    # Enter a parse tree produced by SQLParser#ddl_statement.
    def enterDdl_statement(self, ctx:SQLParser.Ddl_statementContext):
        pass

    # Exit a parse tree produced by SQLParser#ddl_statement.
    def exitDdl_statement(self, ctx:SQLParser.Ddl_statementContext):
        pass


    # Enter a parse tree produced by SQLParser#dml_statement.
    def enterDml_statement(self, ctx:SQLParser.Dml_statementContext):
        pass

    # Exit a parse tree produced by SQLParser#dml_statement.
    def exitDml_statement(self, ctx:SQLParser.Dml_statementContext):
        pass


    # Enter a parse tree produced by SQLParser#create_statement.
    def enterCreate_statement(self, ctx:SQLParser.Create_statementContext):
        pass

    # Exit a parse tree produced by SQLParser#create_statement.
    def exitCreate_statement(self, ctx:SQLParser.Create_statementContext):
        pass


    # Enter a parse tree produced by SQLParser#column_def_list.
    def enterColumn_def_list(self, ctx:SQLParser.Column_def_listContext):
        pass

    # Exit a parse tree produced by SQLParser#column_def_list.
    def exitColumn_def_list(self, ctx:SQLParser.Column_def_listContext):
        pass


    # Enter a parse tree produced by SQLParser#column_def.
    def enterColumn_def(self, ctx:SQLParser.Column_defContext):
        pass

    # Exit a parse tree produced by SQLParser#column_def.
    def exitColumn_def(self, ctx:SQLParser.Column_defContext):
        pass


    # Enter a parse tree produced by SQLParser#data_type.
    def enterData_type(self, ctx:SQLParser.Data_typeContext):
        pass

    # Exit a parse tree produced by SQLParser#data_type.
    def exitData_type(self, ctx:SQLParser.Data_typeContext):
        pass


    # Enter a parse tree produced by SQLParser#column_constraint.
    def enterColumn_constraint(self, ctx:SQLParser.Column_constraintContext):
        pass

    # Exit a parse tree produced by SQLParser#column_constraint.
    def exitColumn_constraint(self, ctx:SQLParser.Column_constraintContext):
        pass


    # Enter a parse tree produced by SQLParser#AlterAdd.
    def enterAlterAdd(self, ctx:SQLParser.AlterAddContext):
        pass

    # Exit a parse tree produced by SQLParser#AlterAdd.
    def exitAlterAdd(self, ctx:SQLParser.AlterAddContext):
        pass


    # Enter a parse tree produced by SQLParser#AlterDrop.
    def enterAlterDrop(self, ctx:SQLParser.AlterDropContext):
        pass

    # Exit a parse tree produced by SQLParser#AlterDrop.
    def exitAlterDrop(self, ctx:SQLParser.AlterDropContext):
        pass


    # Enter a parse tree produced by SQLParser#AlterModify.
    def enterAlterModify(self, ctx:SQLParser.AlterModifyContext):
        pass

    # Exit a parse tree produced by SQLParser#AlterModify.
    def exitAlterModify(self, ctx:SQLParser.AlterModifyContext):
        pass


    # Enter a parse tree produced by SQLParser#drop_statement.
    def enterDrop_statement(self, ctx:SQLParser.Drop_statementContext):
        pass

    # Exit a parse tree produced by SQLParser#drop_statement.
    def exitDrop_statement(self, ctx:SQLParser.Drop_statementContext):
        pass


    # Enter a parse tree produced by SQLParser#truncate_statement.
    def enterTruncate_statement(self, ctx:SQLParser.Truncate_statementContext):
        pass

    # Exit a parse tree produced by SQLParser#truncate_statement.
    def exitTruncate_statement(self, ctx:SQLParser.Truncate_statementContext):
        pass


    # Enter a parse tree produced by SQLParser#use_statement.
    def enterUse_statement(self, ctx:SQLParser.Use_statementContext):
        pass

    # Exit a parse tree produced by SQLParser#use_statement.
    def exitUse_statement(self, ctx:SQLParser.Use_statementContext):
        pass


    # Enter a parse tree produced by SQLParser#select_statement.
    def enterSelect_statement(self, ctx:SQLParser.Select_statementContext):
        pass

    # Exit a parse tree produced by SQLParser#select_statement.
    def exitSelect_statement(self, ctx:SQLParser.Select_statementContext):
        pass


    # Enter a parse tree produced by SQLParser#select_list.
    def enterSelect_list(self, ctx:SQLParser.Select_listContext):
        pass

    # Exit a parse tree produced by SQLParser#select_list.
    def exitSelect_list(self, ctx:SQLParser.Select_listContext):
        pass


    # Enter a parse tree produced by SQLParser#SelectVarAssignment.
    def enterSelectVarAssignment(self, ctx:SQLParser.SelectVarAssignmentContext):
        pass

    # Exit a parse tree produced by SQLParser#SelectVarAssignment.
    def exitSelectVarAssignment(self, ctx:SQLParser.SelectVarAssignmentContext):
        pass


    # Enter a parse tree produced by SQLParser#SelectAliasAssignment.
    def enterSelectAliasAssignment(self, ctx:SQLParser.SelectAliasAssignmentContext):
        pass

    # Exit a parse tree produced by SQLParser#SelectAliasAssignment.
    def exitSelectAliasAssignment(self, ctx:SQLParser.SelectAliasAssignmentContext):
        pass


    # Enter a parse tree produced by SQLParser#SelectExpression.
    def enterSelectExpression(self, ctx:SQLParser.SelectExpressionContext):
        pass

    # Exit a parse tree produced by SQLParser#SelectExpression.
    def exitSelectExpression(self, ctx:SQLParser.SelectExpressionContext):
        pass


    # Enter a parse tree produced by SQLParser#table_source.
    def enterTable_source(self, ctx:SQLParser.Table_sourceContext):
        pass

    # Exit a parse tree produced by SQLParser#table_source.
    def exitTable_source(self, ctx:SQLParser.Table_sourceContext):
        pass


    # Enter a parse tree produced by SQLParser#join_part.
    def enterJoin_part(self, ctx:SQLParser.Join_partContext):
        pass

    # Exit a parse tree produced by SQLParser#join_part.
    def exitJoin_part(self, ctx:SQLParser.Join_partContext):
        pass


    # Enter a parse tree produced by SQLParser#group_list.
    def enterGroup_list(self, ctx:SQLParser.Group_listContext):
        pass

    # Exit a parse tree produced by SQLParser#group_list.
    def exitGroup_list(self, ctx:SQLParser.Group_listContext):
        pass


    # Enter a parse tree produced by SQLParser#order_list.
    def enterOrder_list(self, ctx:SQLParser.Order_listContext):
        pass

    # Exit a parse tree produced by SQLParser#order_list.
    def exitOrder_list(self, ctx:SQLParser.Order_listContext):
        pass


    # Enter a parse tree produced by SQLParser#insert_statement.
    def enterInsert_statement(self, ctx:SQLParser.Insert_statementContext):
        pass

    # Exit a parse tree produced by SQLParser#insert_statement.
    def exitInsert_statement(self, ctx:SQLParser.Insert_statementContext):
        pass


    # Enter a parse tree produced by SQLParser#expression_list_parens.
    def enterExpression_list_parens(self, ctx:SQLParser.Expression_list_parensContext):
        pass

    # Exit a parse tree produced by SQLParser#expression_list_parens.
    def exitExpression_list_parens(self, ctx:SQLParser.Expression_list_parensContext):
        pass


    # Enter a parse tree produced by SQLParser#column_list.
    def enterColumn_list(self, ctx:SQLParser.Column_listContext):
        pass

    # Exit a parse tree produced by SQLParser#column_list.
    def exitColumn_list(self, ctx:SQLParser.Column_listContext):
        pass


    # Enter a parse tree produced by SQLParser#expression_list.
    def enterExpression_list(self, ctx:SQLParser.Expression_listContext):
        pass

    # Exit a parse tree produced by SQLParser#expression_list.
    def exitExpression_list(self, ctx:SQLParser.Expression_listContext):
        pass


    # Enter a parse tree produced by SQLParser#update_statement.
    def enterUpdate_statement(self, ctx:SQLParser.Update_statementContext):
        pass

    # Exit a parse tree produced by SQLParser#update_statement.
    def exitUpdate_statement(self, ctx:SQLParser.Update_statementContext):
        pass


    # Enter a parse tree produced by SQLParser#assignment_list.
    def enterAssignment_list(self, ctx:SQLParser.Assignment_listContext):
        pass

    # Exit a parse tree produced by SQLParser#assignment_list.
    def exitAssignment_list(self, ctx:SQLParser.Assignment_listContext):
        pass


    # Enter a parse tree produced by SQLParser#assignment.
    def enterAssignment(self, ctx:SQLParser.AssignmentContext):
        pass

    # Exit a parse tree produced by SQLParser#assignment.
    def exitAssignment(self, ctx:SQLParser.AssignmentContext):
        pass


    # Enter a parse tree produced by SQLParser#delete_statement.
    def enterDelete_statement(self, ctx:SQLParser.Delete_statementContext):
        pass

    # Exit a parse tree produced by SQLParser#delete_statement.
    def exitDelete_statement(self, ctx:SQLParser.Delete_statementContext):
        pass


    # Enter a parse tree produced by SQLParser#declare_statement.
    def enterDeclare_statement(self, ctx:SQLParser.Declare_statementContext):
        pass

    # Exit a parse tree produced by SQLParser#declare_statement.
    def exitDeclare_statement(self, ctx:SQLParser.Declare_statementContext):
        pass


    # Enter a parse tree produced by SQLParser#declare_list.
    def enterDeclare_list(self, ctx:SQLParser.Declare_listContext):
        pass

    # Exit a parse tree produced by SQLParser#declare_list.
    def exitDeclare_list(self, ctx:SQLParser.Declare_listContext):
        pass


    # Enter a parse tree produced by SQLParser#declare_item.
    def enterDeclare_item(self, ctx:SQLParser.Declare_itemContext):
        pass

    # Exit a parse tree produced by SQLParser#declare_item.
    def exitDeclare_item(self, ctx:SQLParser.Declare_itemContext):
        pass


    # Enter a parse tree produced by SQLParser#set_statement.
    def enterSet_statement(self, ctx:SQLParser.Set_statementContext):
        pass

    # Exit a parse tree produced by SQLParser#set_statement.
    def exitSet_statement(self, ctx:SQLParser.Set_statementContext):
        pass


    # Enter a parse tree produced by SQLParser#control_flow_statement.
    def enterControl_flow_statement(self, ctx:SQLParser.Control_flow_statementContext):
        pass

    # Exit a parse tree produced by SQLParser#control_flow_statement.
    def exitControl_flow_statement(self, ctx:SQLParser.Control_flow_statementContext):
        pass


    # Enter a parse tree produced by SQLParser#print_statement.
    def enterPrint_statement(self, ctx:SQLParser.Print_statementContext):
        pass

    # Exit a parse tree produced by SQLParser#print_statement.
    def exitPrint_statement(self, ctx:SQLParser.Print_statementContext):
        pass


    # Enter a parse tree produced by SQLParser#execute_statement.
    def enterExecute_statement(self, ctx:SQLParser.Execute_statementContext):
        pass

    # Exit a parse tree produced by SQLParser#execute_statement.
    def exitExecute_statement(self, ctx:SQLParser.Execute_statementContext):
        pass


    # Enter a parse tree produced by SQLParser#with_expression.
    def enterWith_expression(self, ctx:SQLParser.With_expressionContext):
        pass

    # Exit a parse tree produced by SQLParser#with_expression.
    def exitWith_expression(self, ctx:SQLParser.With_expressionContext):
        pass


    # Enter a parse tree produced by SQLParser#LikeExpr.
    def enterLikeExpr(self, ctx:SQLParser.LikeExprContext):
        pass

    # Exit a parse tree produced by SQLParser#LikeExpr.
    def exitLikeExpr(self, ctx:SQLParser.LikeExprContext):
        pass


    # Enter a parse tree produced by SQLParser#IsNotNullExpr.
    def enterIsNotNullExpr(self, ctx:SQLParser.IsNotNullExprContext):
        pass

    # Exit a parse tree produced by SQLParser#IsNotNullExpr.
    def exitIsNotNullExpr(self, ctx:SQLParser.IsNotNullExprContext):
        pass


    # Enter a parse tree produced by SQLParser#IsNullExpr.
    def enterIsNullExpr(self, ctx:SQLParser.IsNullExprContext):
        pass

    # Exit a parse tree produced by SQLParser#IsNullExpr.
    def exitIsNullExpr(self, ctx:SQLParser.IsNullExprContext):
        pass


    # Enter a parse tree produced by SQLParser#ComparisonExpr.
    def enterComparisonExpr(self, ctx:SQLParser.ComparisonExprContext):
        pass

    # Exit a parse tree produced by SQLParser#ComparisonExpr.
    def exitComparisonExpr(self, ctx:SQLParser.ComparisonExprContext):
        pass


    # Enter a parse tree produced by SQLParser#BetweenExpr.
    def enterBetweenExpr(self, ctx:SQLParser.BetweenExprContext):
        pass

    # Exit a parse tree produced by SQLParser#BetweenExpr.
    def exitBetweenExpr(self, ctx:SQLParser.BetweenExprContext):
        pass


    # Enter a parse tree produced by SQLParser#AtomExpr.
    def enterAtomExpr(self, ctx:SQLParser.AtomExprContext):
        pass

    # Exit a parse tree produced by SQLParser#AtomExpr.
    def exitAtomExpr(self, ctx:SQLParser.AtomExprContext):
        pass


    # Enter a parse tree produced by SQLParser#MultiplicativeExpr.
    def enterMultiplicativeExpr(self, ctx:SQLParser.MultiplicativeExprContext):
        pass

    # Exit a parse tree produced by SQLParser#MultiplicativeExpr.
    def exitMultiplicativeExpr(self, ctx:SQLParser.MultiplicativeExprContext):
        pass


    # Enter a parse tree produced by SQLParser#FunctionCallExpr.
    def enterFunctionCallExpr(self, ctx:SQLParser.FunctionCallExprContext):
        pass

    # Exit a parse tree produced by SQLParser#FunctionCallExpr.
    def exitFunctionCallExpr(self, ctx:SQLParser.FunctionCallExprContext):
        pass


    # Enter a parse tree produced by SQLParser#AdditiveExpr.
    def enterAdditiveExpr(self, ctx:SQLParser.AdditiveExprContext):
        pass

    # Exit a parse tree produced by SQLParser#AdditiveExpr.
    def exitAdditiveExpr(self, ctx:SQLParser.AdditiveExprContext):
        pass


    # Enter a parse tree produced by SQLParser#NotExpr.
    def enterNotExpr(self, ctx:SQLParser.NotExprContext):
        pass

    # Exit a parse tree produced by SQLParser#NotExpr.
    def exitNotExpr(self, ctx:SQLParser.NotExprContext):
        pass


    # Enter a parse tree produced by SQLParser#InExpr.
    def enterInExpr(self, ctx:SQLParser.InExprContext):
        pass

    # Exit a parse tree produced by SQLParser#InExpr.
    def exitInExpr(self, ctx:SQLParser.InExprContext):
        pass


    # Enter a parse tree produced by SQLParser#ParenExpr.
    def enterParenExpr(self, ctx:SQLParser.ParenExprContext):
        pass

    # Exit a parse tree produced by SQLParser#ParenExpr.
    def exitParenExpr(self, ctx:SQLParser.ParenExprContext):
        pass


    # Enter a parse tree produced by SQLParser#CaseExpr.
    def enterCaseExpr(self, ctx:SQLParser.CaseExprContext):
        pass

    # Exit a parse tree produced by SQLParser#CaseExpr.
    def exitCaseExpr(self, ctx:SQLParser.CaseExprContext):
        pass


    # Enter a parse tree produced by SQLParser#LogicalExpr.
    def enterLogicalExpr(self, ctx:SQLParser.LogicalExprContext):
        pass

    # Exit a parse tree produced by SQLParser#LogicalExpr.
    def exitLogicalExpr(self, ctx:SQLParser.LogicalExprContext):
        pass


    # Enter a parse tree produced by SQLParser#ExistsExpr.
    def enterExistsExpr(self, ctx:SQLParser.ExistsExprContext):
        pass

    # Exit a parse tree produced by SQLParser#ExistsExpr.
    def exitExistsExpr(self, ctx:SQLParser.ExistsExprContext):
        pass


    # Enter a parse tree produced by SQLParser#ScalarSubqueryExpr.
    def enterScalarSubqueryExpr(self, ctx:SQLParser.ScalarSubqueryExprContext):
        pass

    # Exit a parse tree produced by SQLParser#ScalarSubqueryExpr.
    def exitScalarSubqueryExpr(self, ctx:SQLParser.ScalarSubqueryExprContext):
        pass


    # Enter a parse tree produced by SQLParser#function_call.
    def enterFunction_call(self, ctx:SQLParser.Function_callContext):
        pass

    # Exit a parse tree produced by SQLParser#function_call.
    def exitFunction_call(self, ctx:SQLParser.Function_callContext):
        pass


    # Enter a parse tree produced by SQLParser#atom.
    def enterAtom(self, ctx:SQLParser.AtomContext):
        pass

    # Exit a parse tree produced by SQLParser#atom.
    def exitAtom(self, ctx:SQLParser.AtomContext):
        pass


    # Enter a parse tree produced by SQLParser#table_name.
    def enterTable_name(self, ctx:SQLParser.Table_nameContext):
        pass

    # Exit a parse tree produced by SQLParser#table_name.
    def exitTable_name(self, ctx:SQLParser.Table_nameContext):
        pass


    # Enter a parse tree produced by SQLParser#id_name.
    def enterId_name(self, ctx:SQLParser.Id_nameContext):
        pass

    # Exit a parse tree produced by SQLParser#id_name.
    def exitId_name(self, ctx:SQLParser.Id_nameContext):
        pass


    # Enter a parse tree produced by SQLParser#constant.
    def enterConstant(self, ctx:SQLParser.ConstantContext):
        pass

    # Exit a parse tree produced by SQLParser#constant.
    def exitConstant(self, ctx:SQLParser.ConstantContext):
        pass


    # Enter a parse tree produced by SQLParser#variable.
    def enterVariable(self, ctx:SQLParser.VariableContext):
        pass

    # Exit a parse tree produced by SQLParser#variable.
    def exitVariable(self, ctx:SQLParser.VariableContext):
        pass



del SQLParser