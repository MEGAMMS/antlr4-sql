from __future__ import annotations

from src.antlr_generated.SQLParserVisitor import SQLParserVisitor
from src.antlr_generated.SQLParser import SQLParser

from src.sql_ast.base import ExpressionNode
from src.sql_ast.expressions import (
    BinaryExpressionNode,
    UnaryExpressionNode,
    VariableNode,
    StarNode,
    FunctionCallNode,
    BetweenExpressionNode,
    InExpressionNode,
    LikeExpressionNode,
    IsNullExpressionNode,
    ExistsExpressionNode,
    CaseExpressionNode,
    WhenClauseNode,
)
from src.sql_ast.statements import (
    ProgramNode,
    SelectNode,
    TableNode,
    IdentifierNode,
    LiteralNode,
    OrderByNode,
    WithNode,
    CteNode,
    SelectItemNode,
    SelectVarAssignNode,
    TableSourceNode,
    JoinNode,
    ValueListNode,
    InsertStatement,
    AssignmentNode,
    UpdateStatement,
    DeleteStatement,
    DataTypeNode,
    ColumnConstraintNode,
    ColumnDefNode,
    TableConstraintNode,
    TableReferenceNode,
    CreateTableNode,
    AlterTableNode,
    DropStatementNode,
    TruncateStatementNode,
    UseStatementNode,
    PrintStatementNode,
    SetStatementNode,
    DeclareStatementNode,
    DeclaredVariableNode,
    CursorDeclareNode,
    OpenCursorNode,
    FetchCursorNode,
    CloseCursorNode,
    DeallocateCursorNode,
    BlockNode,
    IfStatementNode,
    TryCatchNode,
    ExecuteNode,
)


class ASTBuilder(SQLParserVisitor):
    """Builds an abstract syntax tree from the parse tree."""

    def visitRoot(self, ctx: SQLParser.RootContext):
        statements = self.visit(ctx.sql_script())
        return ProgramNode(statements)

    def visitSql_script(self, ctx: SQLParser.Sql_scriptContext):
        statements = []
        for batch in ctx.batch():
            result = self.visit(batch)
            if isinstance(result, list):
                statements.extend(result)
            elif result:
                statements.append(result)
        return statements

    def visitStatementBatch(self, ctx: SQLParser.StatementBatchContext):
        statements = []
        for stmt in ctx.sql_statement():
            node = self.visit(stmt)
            if node:
                if isinstance(node, list):
                    statements.extend(node)
                else:
                    statements.append(node)
        return statements

    def visitEmptyGo(self, ctx: SQLParser.EmptyGoContext):
        return []

    # SQL statements -------------------------------------------------
    def visitSql_statement(self, ctx: SQLParser.Sql_statementContext):
        if ctx.ddl_statement():
            return self.visit(ctx.ddl_statement())
        if ctx.dml_statement():
            return self.visit(ctx.dml_statement())
        if ctx.cursor_statement():
            return self.visit(ctx.cursor_statement())
        if ctx.control_flow_statement():
            return self.visit(ctx.control_flow_statement())
        if ctx.print_statement():
            return self.visit(ctx.print_statement())
        if ctx.declare_statement():
            return self.visit(ctx.declare_statement())
        if ctx.set_statement():
            return self.visit(ctx.set_statement())
        if ctx.execute_statement():
            return self.visit(ctx.execute_statement())
        return None

    def visitDdl_statement(self, ctx: SQLParser.Ddl_statementContext):
        for rule in [
            ctx.create_statement,
            ctx.alter_statement,
            ctx.drop_statement,
            ctx.truncate_statement,
            ctx.use_statement,
        ]:
            if rule():
                return self.visit(rule())
        return None

    def visitDml_statement(self, ctx: SQLParser.Dml_statementContext):
        with_clause = self.visit(ctx.with_expression()) if ctx.with_expression() else None

        if ctx.select_statement():
            node = self.visit(ctx.select_statement())
            if with_clause and isinstance(node, SelectNode) and node.with_clause is None:
                node.with_clause = with_clause
            return node
        if ctx.insert_statement():
            stmt = self.visit(ctx.insert_statement())
            if with_clause:
                stmt.with_clause = with_clause
            return stmt
        if ctx.update_statement():
            stmt = self.visit(ctx.update_statement())
            if with_clause:
                stmt.with_clause = with_clause
            return stmt
        if ctx.delete_statement():
            stmt = self.visit(ctx.delete_statement())
            if with_clause:
                stmt.with_clause = with_clause
            return stmt
        return None

    # DDL -------------------------------------------------------------
    def visitCreate_statement(self, ctx: SQLParser.Create_statementContext):
        table = self.visit(ctx.table_name())
        elements = self.visit(ctx.table_element_list())
        return CreateTableNode(table, elements)

    def visitTable_element_list(self, ctx: SQLParser.Table_element_listContext):
        return [self.visit(el) for el in ctx.table_element()]

    def visitTable_element(self, ctx: SQLParser.Table_elementContext):
        if ctx.column_def():
            return self.visit(ctx.column_def())
        return self.visit(ctx.table_constraint())

    def visitColumn_def(self, ctx: SQLParser.Column_defContext):
        name = self.visit(ctx.id_name())
        data_type = self.visit(ctx.data_type())
        constraints = [self.visit(c) for c in ctx.column_constraint()]
        return ColumnDefNode(name, data_type, constraints)

    def visitData_type(self, ctx: SQLParser.Data_typeContext):
        id_parts = self._as_list(ctx.id_name())
        name_ctx = id_parts[0]
        param_id_ctx = id_parts[1] if len(id_parts) > 1 else None

        name = self._text_from_id(name_ctx)

        params = []
        for tok in ctx.INT():
            params.append(LiteralNode(int(tok.getText())))
        if param_id_ctx:
            params.append(self.visit(param_id_ctx))
        return DataTypeNode(name, params)

    def visitColumn_constraint(self, ctx: SQLParser.Column_constraintContext):
        if ctx.PRIMARY():
            text = "PRIMARY KEY"
        elif ctx.UNIQUE():
            text = "UNIQUE"
        elif ctx.NOT() and ctx.NULL():
            text = "NOT NULL"
        elif ctx.NULL():
            text = "NULL"
        else:
            text = ctx.getChild(0).getText().upper()
        if ctx.DEFAULT():
            return ColumnConstraintNode("DEFAULT", self.visit(ctx.expression()))
        if ctx.IDENTITY():
            return ColumnConstraintNode("IDENTITY")
        if ctx.REFERENCES():
            table = self.visit(ctx.table_name())
            ref_col = self.visit(ctx.id_name())
            details = TableReferenceNode(table, [ref_col])
            return ColumnConstraintNode("REFERENCES", details)
        return ColumnConstraintNode(text)

    def visitTable_constraint(self, ctx: SQLParser.Table_constraintContext):
        constraint_name = self.visit(ctx.id_name()) if ctx.CONSTRAINT() else None
        if ctx.PRIMARY():
            cols = self.visit(ctx.column_list(0))
            return TableConstraintNode("PRIMARY KEY", cols, name=constraint_name)
        if ctx.UNIQUE():
            cols = self.visit(ctx.column_list(0))
            return TableConstraintNode("UNIQUE", cols, name=constraint_name)
        if ctx.FOREIGN():
            cols = self.visit(ctx.column_list(0))
            ref_table = self.visit(ctx.table_name())
            ref_cols = self.visit(ctx.column_list(1))
            reference = TableReferenceNode(ref_table, ref_cols)
            return TableConstraintNode("FOREIGN KEY", cols, reference=reference, name=constraint_name)
        if ctx.CHECK():
            condition = self.visit(ctx.expression())
            return TableConstraintNode("CHECK", condition=condition, name=constraint_name)
        return TableConstraintNode("CONSTRAINT", name=constraint_name)

    def visitAlterAdd(self, ctx: SQLParser.AlterAddContext):
        table = self.visit(ctx.table_name())
        column = self.visit(ctx.column_def())
        return AlterTableNode(table, "ADD", column)

    def visitAlterDrop(self, ctx: SQLParser.AlterDropContext):
        table = self.visit(ctx.table_name())
        column = self.visit(ctx.id_name())
        return AlterTableNode(table, "DROP COLUMN", column)

    def visitAlterModify(self, ctx: SQLParser.AlterModifyContext):
        table = self.visit(ctx.table_name())
        column = self.visit(ctx.column_def())
        return AlterTableNode(table, "ALTER COLUMN", column)

    def visitDrop_statement(self, ctx: SQLParser.Drop_statementContext):
        obj = ctx.getChild(1).getText().upper()
        name = self.visit(ctx.table_name())
        return DropStatementNode(obj, name)

    def visitTruncate_statement(self, ctx: SQLParser.Truncate_statementContext):
        return TruncateStatementNode(self.visit(ctx.table_name()))

    def visitUse_statement(self, ctx: SQLParser.Use_statementContext):
        return UseStatementNode(self.visit(ctx.id_name()))

    # DML -------------------------------------------------------------
    def visitSelect_statement(self, ctx: SQLParser.Select_statementContext):
        with_clause = self.visit(ctx.with_expression()) if ctx.with_expression() else None
        distinct = ctx.DISTINCT() is not None
        top_value = None
        if ctx.TOP():
            top_value = LiteralNode(int(ctx.INT().getText()))

        select_list = self.visit(ctx.select_list())

        from_clause = None
        joins = []
        where_clause = None
        group_by = []
        having_clause = None
        order_by = []

        exprs = list(ctx.expression())

        if ctx.table_source():
            from_clause = self.visit(ctx.table_source())
        if ctx.join_part():
            joins = [self.visit(j) for j in ctx.join_part()]
        if ctx.WHERE():
            where_clause = self.visit(exprs[0])
        if ctx.GROUP():
            group_by = self.visit(ctx.group_list())
        if ctx.HAVING():
            having_clause = self.visit(exprs[-1])
        if ctx.order_list():
            order_by = self.visit(ctx.order_list())

        return SelectNode(
            select_list=select_list,
            from_clause=from_clause,
            joins=joins,
            where_clause=where_clause,
            group_by=group_by,
            having_clause=having_clause,
            order_by=order_by,
            distinct=distinct,
            top=top_value,
            with_clause=with_clause,
        )

    def visitSelect_list(self, ctx: SQLParser.Select_listContext):
        if ctx.STAR():
            return [StarNode()]
        return [self.visit(i) for i in ctx.select_item()]

    def visitSelectVarAssignment(self, ctx: SQLParser.SelectVarAssignmentContext):
        var = self.visit(ctx.variable())
        op = ctx.getChild(1).getText()
        expr = self.visit(ctx.expression())
        return SelectVarAssignNode(var, op, expr)

    def visitSelectAliasAssignment(self, ctx: SQLParser.SelectAliasAssignmentContext):
        alias = self.visit(ctx.id_name())
        expr = self.visit(ctx.expression())
        return SelectItemNode(expr, alias.name)

    def visitSelectExpression(self, ctx: SQLParser.SelectExpressionContext):
        expr = self.visit(ctx.expression())
        alias = None
        if ctx.alias_name():
            alias_node = self.visit(ctx.alias_name())
            if hasattr(alias_node, "name"):
                alias = alias_node.name
            elif hasattr(alias_node, "value"):
                alias = alias_node.value
            else:
                alias = str(alias_node)
        return SelectItemNode(expr, alias)

    def visitTable_source(self, ctx: SQLParser.Table_sourceContext):
        alias = self.visit(ctx.id_name()) if ctx.id_name() else None
        if ctx.table_name():
            source = self.visit(ctx.table_name())
            return TableSourceNode(source, alias)
        inner = self.visit(ctx.select_statement())
        return TableSourceNode(inner, alias)

    def visitJoin_part(self, ctx: SQLParser.Join_partContext):
        join_parts = []
        if ctx.INNER():
            join_parts.append("INNER")
        elif ctx.LEFT():
            join_parts.append("LEFT")
        elif ctx.RIGHT():
            join_parts.append("RIGHT")
        elif ctx.FULL():
            join_parts.append("FULL")
        elif ctx.CROSS():
            join_parts.append("CROSS")
        if ctx.OUTER():
            join_parts.append("OUTER")
        join_parts.append("JOIN")
        join_type = " ".join(join_parts)
        table_source = self.visit(ctx.table_source())
        condition = self.visit(ctx.expression())
        return JoinNode(join_type, table_source, condition)

    def visitGroup_list(self, ctx: SQLParser.Group_listContext):
        return [self.visit(expr) for expr in ctx.expression()]

    def visitOrder_list(self, ctx: SQLParser.Order_listContext):
        items = []
        expressions = ctx.expression()
        for expr in expressions:
            direction = "ASC"
            idx = ctx.children.index(expr)
            if idx + 1 < len(ctx.children):
                nxt = ctx.children[idx + 1]
                if hasattr(nxt, "getText"):
                    text = nxt.getText().upper()
                    if text in ("ASC", "DESC"):
                        direction = text
            items.append(OrderByNode(self.visit(expr), direction))
        return items

    def visitInsert_statement(self, ctx: SQLParser.Insert_statementContext):
        table = self.visit(ctx.table_name())
        columns = self.visit(ctx.column_list()) if ctx.column_list() else []
        if ctx.VALUES():
            values = [self.visit(v) for v in ctx.expression_list_parens()]
            return InsertStatement(table, columns, values=values)
        select_query = self.visit(ctx.select_statement())
        return InsertStatement(table, columns, select_query=select_query)

    def visitExpression_list_parens(self, ctx: SQLParser.Expression_list_parensContext):
        return ValueListNode(self.visit(ctx.expression_list()))

    def visitColumn_list(self, ctx: SQLParser.Column_listContext):
        return [self.visit(c) for c in ctx.id_name()]

    def visitExpression_list(self, ctx: SQLParser.Expression_listContext):
        return [self.visit(e) for e in ctx.expression()]

    def visitUpdate_statement(self, ctx: SQLParser.Update_statementContext):
        table = self.visit(ctx.table_name())
        assignments = self.visit(ctx.assignment_list())
        where_clause = self.visit(ctx.expression()) if ctx.WHERE() else None
        return UpdateStatement(table, assignments, where_clause=where_clause)

    def visitAssignment_list(self, ctx: SQLParser.Assignment_listContext):
        return [self.visit(a) for a in ctx.assignment()]

    def visitAssignment(self, ctx: SQLParser.AssignmentContext):
        target = self.visit(ctx.id_name())
        op = ctx.getChild(1).getText()
        value = self.visit(ctx.expression())
        return AssignmentNode(target, op, value)

    def visitDelete_statement(self, ctx: SQLParser.Delete_statementContext):
        table = self.visit(ctx.table_name())
        where_clause = self.visit(ctx.expression()) if ctx.WHERE() else None
        return DeleteStatement(table, where_clause=where_clause)

    # Variables and control flow -------------------------------------
    def visitDeclare_statement(self, ctx: SQLParser.Declare_statementContext):
        if ctx.cursor_declare_statement():
            return self.visit(ctx.cursor_declare_statement())
        return DeclareStatementNode(self.visit(ctx.declare_list()))

    def visitDeclare_list(self, ctx: SQLParser.Declare_listContext):
        return [self.visit(item) for item in ctx.declare_item()]

    def visitDeclare_item(self, ctx: SQLParser.Declare_itemContext):
        name = self.visit(ctx.LOCAL_VAR())
        data_type = self.visit(ctx.data_type())
        default_value = self.visit(ctx.expression()) if ctx.expression() else None
        return DeclaredVariableNode(name, data_type, default_value)

    def visitSet_statement(self, ctx: SQLParser.Set_statementContext):
        var = self.visit(ctx.variable())
        op = ctx.getChild(1).getText()
        expr = self.visit(ctx.expression())
        return SetStatementNode(var, op, expr)

    def visitCursor_declare_statement(self, ctx: SQLParser.Cursor_declare_statementContext):
        name = self.visit(ctx.id_name())
        query = self.visit(ctx.select_statement())
        return CursorDeclareNode(name, query)

    def visitOpen_cursor_statement(self, ctx: SQLParser.Open_cursor_statementContext):
        return OpenCursorNode(self.visit(ctx.id_name()))

    def visitFetch_cursor_statement(self, ctx: SQLParser.Fetch_cursor_statementContext):
        name = self.visit(ctx.id_name())
        variables = self.visit(ctx.variable_list()) if ctx.variable_list() else []
        return FetchCursorNode(name, variables)

    def visitVariable_list(self, ctx: SQLParser.Variable_listContext):
        return [self.visit(v) for v in ctx.variable()]

    def visitClose_cursor_statement(self, ctx: SQLParser.Close_cursor_statementContext):
        return CloseCursorNode(self.visit(ctx.id_name()))

    def visitDeallocate_cursor_statement(self, ctx: SQLParser.Deallocate_cursor_statementContext):
        return DeallocateCursorNode(self.visit(ctx.id_name()))

    def visitBlock(self, ctx: SQLParser.BlockContext):
        statements = []
        for stmt in ctx.sql_statement():
            node = self.visit(stmt)
            if node:
                if isinstance(node, list):
                    statements.extend(node)
                else:
                    statements.append(node)
        return BlockNode(statements)

    def visitBegin_block(self, ctx: SQLParser.Begin_blockContext):
        return self.visit(ctx.block())

    def visitIf_statement(self, ctx: SQLParser.If_statementContext):
        condition = self.visit(ctx.expression())
        then_block = self.visit(ctx.sql_statement(0))
        else_block = self.visit(ctx.sql_statement(1)) if ctx.ELSE() else None
        return IfStatementNode(condition, then_block, else_block)

    def visitTry_catch(self, ctx: SQLParser.Try_catchContext):
        try_block = self.visit(ctx.block(0))
        catch_block = self.visit(ctx.block(1))
        return TryCatchNode(try_block, catch_block)

    def visitExecute_statement(self, ctx: SQLParser.Execute_statementContext):
        output_var = self.visit(ctx.variable()) if ctx.variable() and ctx.EQ() else None
        target = self.visit(ctx.table_name()) if ctx.table_name() else self.visit(ctx.variable(0))
        args = []
        if ctx.expression():
            args = [self.visit(e) for e in ctx.expression()]
        return ExecuteNode(target, args, output_variable=output_var)

    def visitPrint_statement(self, ctx: SQLParser.Print_statementContext):
        return PrintStatementNode(self.visit(ctx.expression()))

    # Expressions -----------------------------------------------------
    def visitLogicalOrExpr(self, ctx: SQLParser.LogicalOrExprContext):
        if len(ctx.logical_and_expression()) == 1:
            return self.visit(ctx.logical_and_expression(0))
        exprs = [self.visit(e) for e in ctx.logical_and_expression()]
        node = exprs[0]
        for rhs in exprs[1:]:
            node = BinaryExpressionNode("OR", node, rhs)
        return node

    def visitLogicalAndExpr(self, ctx: SQLParser.LogicalAndExprContext):
        if len(ctx.not_expression()) == 1:
            return self.visit(ctx.not_expression(0))
        exprs = [self.visit(e) for e in ctx.not_expression()]
        node = exprs[0]
        for rhs in exprs[1:]:
            node = BinaryExpressionNode("AND", node, rhs)
        return node

    def visitNotExpr(self, ctx: SQLParser.NotExprContext):
        return UnaryExpressionNode("NOT", self.visit(ctx.not_expression()))

    def visitPredicateExpr(self, ctx: SQLParser.PredicateExprContext):
        return self.visit(ctx.comparison_expression())

    def visitComparisonExpr(self, ctx: SQLParser.ComparisonExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.additive_expression(0))
        left = self.visit(ctx.additive_expression(0))
        right = self.visit(ctx.additive_expression(1))
        op = ctx.getChild(1).getText().upper()
        return BinaryExpressionNode(op, left, right)

    def visitBetweenExpr(self, ctx: SQLParser.BetweenExprContext):
        val = self.visit(ctx.additive_expression(0))
        low = self.visit(ctx.additive_expression(1))
        high = self.visit(ctx.additive_expression(2))
        negated = ctx.NOT() is not None
        return BetweenExpressionNode(val, low, high, negated)

    def visitInExpr(self, ctx: SQLParser.InExprContext):
        add_exprs = ctx.additive_expression()
        val_ctx = add_exprs[0] if isinstance(add_exprs, list) else add_exprs
        val = self.visit(val_ctx)
        negated = ctx.NOT() is not None
        if ctx.select_statement():
            options = self.visit(ctx.select_statement())
        else:
            options = self.visit(ctx.expression_list())
        return InExpressionNode(val, options, negated)

    def visitLikeExpr(self, ctx: SQLParser.LikeExprContext):
        val = self.visit(ctx.additive_expression(0))
        pattern = self.visit(ctx.additive_expression(1))
        negated = ctx.NOT() is not None
        return LikeExpressionNode(val, pattern, negated)

    def visitIsNullExpr(self, ctx: SQLParser.IsNullExprContext):
        val = self.visit(ctx.additive_expression())
        negated = ctx.NOT() is not None
        return IsNullExpressionNode(val, negated)

    def visitValueExpr(self, ctx: SQLParser.ValueExprContext):
        return self.visit(ctx.additive_expression())

    def visitAdditiveExpr(self, ctx: SQLParser.AdditiveExprContext):
        terms = list(ctx.multiplicative_expression())
        ops = list(ctx.getChildren())[1::2]
        node = self.visit(terms[0])
        for op_tok, rhs_ctx in zip(ops, terms[1:]):
            node = BinaryExpressionNode(op_tok.getText(), node, self.visit(rhs_ctx))
        return node

    def visitMultiplicativeExpr(self, ctx: SQLParser.MultiplicativeExprContext):
        factors = list(ctx.unary_expression())
        ops = list(ctx.getChildren())[1::2]
        node = self.visit(factors[0])
        for op_tok, rhs_ctx in zip(ops, factors[1:]):
            node = BinaryExpressionNode(op_tok.getText(), node, self.visit(rhs_ctx))
        return node

    def visitUnaryExpr(self, ctx: SQLParser.UnaryExprContext):
        op = ctx.getChild(0).getText()
        operand = self.visit(ctx.unary_expression())
        return UnaryExpressionNode(op, operand)

    def visitPrimaryUnaryExpr(self, ctx: SQLParser.PrimaryUnaryExprContext):
        return self.visit(ctx.primary_expression())

    def visitParenExpr(self, ctx: SQLParser.ParenExprContext):
        return self.visit(ctx.expression())

    def visitScalarSubqueryExpr(self, ctx: SQLParser.ScalarSubqueryExprContext):
        return self.visit(ctx.select_statement())

    def visitExistsExpr(self, ctx: SQLParser.ExistsExprContext):
        return ExistsExpressionNode(self.visit(ctx.select_statement()))

    def visitCaseExpr(self, ctx: SQLParser.CaseExprContext):
        exprs = list(ctx.expression())
        else_expr = exprs[-1] if ctx.ELSE() else None
        pair_exprs = exprs[:-1] if else_expr is not None else exprs
        whens = []
        for cond_ctx, res_ctx in zip(pair_exprs[0::2], pair_exprs[1::2]):
            whens.append(WhenClauseNode(self.visit(cond_ctx), self.visit(res_ctx)))
        return CaseExpressionNode(whens, self.visit(else_expr) if else_expr is not None else None)

    def visitFunctionCallExpr(self, ctx: SQLParser.FunctionCallExprContext):
        return self.visit(ctx.function_call())

    def visitAtomExpr(self, ctx: SQLParser.AtomExprContext):
        return self.visit(ctx.atom())

    def visitFunction_call(self, ctx: SQLParser.Function_callContext):
        name = self._text_from_id(ctx.id_name())
        args = []
        if ctx.expression_list():
            args = self.visit(ctx.expression_list())
        elif ctx.STAR():
            args = [StarNode()]
        return FunctionCallNode(name, args)

    def visitAtom(self, ctx: SQLParser.AtomContext):
        if ctx.table_name():
            return self.visit(ctx.table_name())
        if ctx.constant():
            return self.visit(ctx.constant())
        return self.visit(ctx.variable())

    # Identifiers / variables -----------------------------------------
    def visitTable_name(self, ctx: SQLParser.Table_nameContext):
        return TableNode([self.visit(idn) for idn in ctx.id_name()])

    def visitId_name(self, ctx: SQLParser.Id_nameContext):
        return IdentifierNode(self._text_from_id(ctx))

    def visitAlias_name(self, ctx: SQLParser.Alias_nameContext):
        return self.visit(ctx.getChild(0))

    def visitConstant(self, ctx: SQLParser.ConstantContext):
        if ctx.INT():
            return LiteralNode(int(ctx.INT().getText()))
        if ctx.FLOAT():
            return LiteralNode(float(ctx.FLOAT().getText()))
        if ctx.STRING():
            text = ctx.STRING().getText()
            return LiteralNode(text[1:-1])
        if ctx.NSTRING():
            text = ctx.NSTRING().getText()
            return LiteralNode(text[2:-1])
        if ctx.TRUE():
            return LiteralNode(True)
        if ctx.FALSE():
            return LiteralNode(False)
        if ctx.NULL():
            return LiteralNode(None)
        return LiteralNode(ctx.getText())

    def visitVariable(self, ctx: SQLParser.VariableContext):
        return VariableNode(ctx.getText())

    # Helpers ---------------------------------------------------------
    def _as_list(self, ctx):
        if isinstance(ctx, list):
            return ctx
        return [ctx]

    def _text_from_id(self, ctx):
        if hasattr(ctx, "getText"):
            return ctx.getText()
        if isinstance(ctx, IdentifierNode):
            return ctx.name
        return str(ctx)
