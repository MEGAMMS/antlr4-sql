from antlr4 import *
from antlr4.tree.Tree import TerminalNode
from src.antlr_generated.SQLParserVisitor import SQLParserVisitor
from src.antlr_generated.SQLParser import SQLParser

from grammar.AST.ProgramNode import ProgramNode
from grammar.AST.SelectNode import SelectNode
from grammar.AST.TableNode import TableNode
from grammar.AST.IdentifierNode import IdentifierNode
from grammar.AST.Literals import LiteralNode
from grammar.AST.BinaryExpressionNode import BinaryExpressionNode
from grammar.AST.UnaryExpressionNode import UnaryExpressionNode
from grammar.AST.OrderByNode import OrderByNode
from grammar.AST.ExpressionNode import ExpressionNode
from grammar.AST.statement_nodes import (
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
from grammar.AST.expression_nodes import (
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
            details = TableConstraintNode("REFERENCES", columns=[ref_col], reference=table)
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
            return TableConstraintNode("FOREIGN KEY", cols, reference=ref_table, name=constraint_name)
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

        from_clause = self.visit(ctx.table_source()) if ctx.table_source() else None
        joins = [self.visit(j) for j in ctx.join_part()] if ctx.join_part() else []
        exprs = ctx.expression()
        expr_idx = 0
        where_clause = None
        having_clause = None
        if ctx.WHERE():
            where_clause = self.visit(exprs[expr_idx])
            expr_idx += 1
        group_by = self.visit(ctx.group_list()) if ctx.GROUP() else []
        if ctx.HAVING():
            having_clause = self.visit(exprs[expr_idx])
        order_by = self.visit(ctx.order_list()) if ctx.order_list() else []

        return SelectNode(
            select_list,
            from_clause,
            joins,
            where_clause,
            group_by,
            having_clause,
            order_by,
            distinct,
            top_value,
            with_clause,
        )

    def visitSelect_list(self, ctx: SQLParser.Select_listContext):
        if ctx.STAR():
            return [StarNode()]
        return [self.visit(item) for item in ctx.select_item()]

    def visitSelectVarAssignment(self, ctx: SQLParser.SelectVarAssignmentContext):
        variable = self.visit(ctx.variable())
        op = ctx.getChild(1).getText()
        expr = self.visit(ctx.expression())
        return SelectVarAssignNode(variable, op, expr)

    def visitSelectAliasAssignment(self, ctx: SQLParser.SelectAliasAssignmentContext):
        alias = self.visit(ctx.id_name())
        expr = self.visit(ctx.expression())
        return SelectItemNode(expr, alias.name)

    def visitSelectExpression(self, ctx: SQLParser.SelectExpressionContext):
        expr = self.visit(ctx.expression())
        alias = self.visit(ctx.id_name()).name if ctx.id_name() else None
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
        values = []
        select_query = None

        if ctx.VALUES():
            for value_ctx in ctx.expression_list_parens():
                values.append(ValueListNode(self.visit(value_ctx.expression_list())))
        else:
            select_query = self.visit(ctx.select_statement())
        return InsertStatement(table, columns, values, select_query)

    def visitColumn_list(self, ctx: SQLParser.Column_listContext):
        return [self.visit(idc) for idc in ctx.id_name()]

    def visitExpression_list(self, ctx: SQLParser.Expression_listContext):
        return [self.visit(expr) for expr in ctx.expression()]

    def visitUpdate_statement(self, ctx: SQLParser.Update_statementContext):
        table = self.visit(ctx.table_name())
        assignments = self.visit(ctx.assignment_list())
        where_clause = self.visit(ctx.expression()) if ctx.WHERE() else None
        return UpdateStatement(table, assignments, where_clause)

    def visitAssignment_list(self, ctx: SQLParser.Assignment_listContext):
        return [self.visit(a) for a in ctx.assignment()]

    def visitAssignment(self, ctx: SQLParser.AssignmentContext):
        target = self.visit(ctx.id_name())
        operator = ctx.getChild(1).getText()
        value = self.visit(ctx.expression())
        return AssignmentNode(target, operator, value)

    def visitDelete_statement(self, ctx: SQLParser.Delete_statementContext):
        table = self.visit(ctx.table_name())
        where_clause = self.visit(ctx.expression()) if ctx.WHERE() else None
        return DeleteStatement(table, where_clause)

    # Variables and SET/DECLARE --------------------------------------
    def visitDeclare_statement(self, ctx: SQLParser.Declare_statementContext):
        if ctx.cursor_declare_statement():
            return self.visit(ctx.cursor_declare_statement())
        items = [self.visit(item) for item in ctx.declare_list().declare_item()]
        return DeclareStatementNode(items)

    def visitCursor_declare_statement(self, ctx: SQLParser.Cursor_declare_statementContext):
        name = self.visit(ctx.id_name())
        query = self.visit(ctx.select_statement())
        return CursorDeclareNode(name, query)

    def visitDeclare_item(self, ctx: SQLParser.Declare_itemContext):
        var = VariableNode(ctx.LOCAL_VAR().getText())
        data_type = self.visit(ctx.data_type())
        default_value = self.visit(ctx.expression()) if ctx.expression() else None
        return DeclaredVariableNode(var, data_type, default_value)

    def visitSet_statement(self, ctx: SQLParser.Set_statementContext):
        variable = self.visit(ctx.variable())
        operator = ctx.getChild(2).getText()
        expression = self.visit(ctx.expression())
        return SetStatementNode(variable, operator, expression)

    # Cursor statements -----------------------------------------------
    def visitCursor_statement(self, ctx: SQLParser.Cursor_statementContext):
        for rule in [
            ctx.open_cursor_statement,
            ctx.fetch_cursor_statement,
            ctx.close_cursor_statement,
            ctx.deallocate_cursor_statement,
        ]:
            if rule():
                return self.visit(rule())
        return None

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

    # Control flow & misc ---------------------------------------------
    def visitControl_flow_statement(self, ctx: SQLParser.Control_flow_statementContext):
        if ctx.TRY():
            in_catch = False
            try_stmts, catch_stmts = [], []
            for child in ctx.children:
                if isinstance(child, TerminalNode) and child.getText().upper() == "CATCH":
                    in_catch = True
                if isinstance(child, SQLParser.Sql_statementContext):
                    node = self.visit(child)
                    if node:
                        (catch_stmts if in_catch else try_stmts).append(node)
            return TryCatchNode(BlockNode(try_stmts), BlockNode(catch_stmts))
        if ctx.BEGIN():
            statements = self._collect_statements(ctx.sql_statement())
            return BlockNode(statements)
        if ctx.IF():
            stmts = ctx.sql_statement()
            condition = self.visit(ctx.expression())
            then_stmt = self.visit(stmts[0])
            else_stmt = self.visit(stmts[1]) if len(stmts) > 1 else None
            then_block = then_stmt if isinstance(then_stmt, BlockNode) else BlockNode([then_stmt])
            else_block = else_stmt if isinstance(else_stmt, BlockNode) else (BlockNode([else_stmt]) if else_stmt else None)
            return IfStatementNode(condition, then_block, else_block)
        return None

    def _collect_statements(self, stmt_list):
        statements = []
        for stmt in stmt_list:
            res = self.visit(stmt)
            if res is None:
                continue
            if isinstance(res, list):
                statements.extend(res)
            else:
                statements.append(res)
        return statements

    def visitPrint_statement(self, ctx: SQLParser.Print_statementContext):
        return PrintStatementNode(self.visit(ctx.expression()))

    def visitExecute_statement(self, ctx: SQLParser.Execute_statementContext):
        variables = ctx.variable()
        output_var = None
        target = None
        if ctx.EQ():
            output_var = self.visit(variables[0])
            target = self.visit(ctx.table_name()) if ctx.table_name() else self.visit(variables[1])
        else:
            if ctx.table_name():
                target = self.visit(ctx.table_name())
            elif variables:
                target = self.visit(variables[0])
        args = [self.visit(expr) for expr in ctx.expression()] if ctx.expression() else []
        return ExecuteNode(target, args, output_var)

    # WITH / CTE ------------------------------------------------------
    def visitWith_expression(self, ctx: SQLParser.With_expressionContext):
        ctes = [self.visit(c) for c in ctx.cte_definition()]
        return WithNode(ctes)

    def visitCte_definition(self, ctx: SQLParser.Cte_definitionContext):
        name = self.visit(ctx.id_name())
        columns = self.visit(ctx.column_list()) if ctx.column_list() else []
        query = self.visit(ctx.select_statement())
        return CteNode(name, columns, query)

    # Expressions -----------------------------------------------------
    def visitLogicalOrExpr(self, ctx: SQLParser.LogicalOrExprContext):
        nodes = [self.visit(c) for c in ctx.logical_and_expression()]
        return self._fold_left(nodes, "OR")

    def visitLogicalAndExpr(self, ctx: SQLParser.LogicalAndExprContext):
        nodes = [self.visit(c) for c in ctx.not_expression()]
        return self._fold_left(nodes, "AND")

    def visitNotExpr(self, ctx: SQLParser.NotExprContext):
        return UnaryExpressionNode("NOT", self.visit(ctx.not_expression()))

    def visitPredicateExpr(self, ctx: SQLParser.PredicateExprContext):
        return self.visit(ctx.comparison_expression())

    def visitComparisonExpr(self, ctx: SQLParser.ComparisonExprContext):
        left = self.visit(ctx.additive_expression(0))
        right = self.visit(ctx.additive_expression(1))
        op = ctx.getChild(1).getText()
        return BinaryExpressionNode(op, left, right)

    def visitBetweenExpr(self, ctx: SQLParser.BetweenExprContext):
        val = self.visit(ctx.additive_expression(0))
        low = self.visit(ctx.additive_expression(1))
        high = self.visit(ctx.additive_expression(2))
        negated = ctx.NOT() is not None
        return BetweenExpressionNode(val, low, high, negated)

    def visitInExpr(self, ctx: SQLParser.InExprContext):
        val = self.visit(ctx.additive_expression())
        negated = ctx.NOT() is not None
        if ctx.expression_list():
            options = self.visit(ctx.expression_list())
        else:
            options = self.visit(ctx.select_statement())
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
        nodes = [self.visit(c) for c in ctx.multiplicative_expression()]
        ops = [child.getText() for child in ctx.children if child.getText() in ("+", "-")]
        return self._fold_with_ops(nodes, ops)

    def visitMultiplicativeExpr(self, ctx: SQLParser.MultiplicativeExprContext):
        nodes = [self.visit(c) for c in ctx.unary_expression()]
        ops = [child.getText() for child in ctx.children if child.getText() in ("*", "/", "%")]
        return self._fold_with_ops(nodes, ops)

    def visitUnaryExpr(self, ctx: SQLParser.UnaryExprContext):
        op = ctx.getChild(0).getText()
        return UnaryExpressionNode(op, self.visit(ctx.unary_expression()))

    def visitPrimaryUnaryExpr(self, ctx: SQLParser.PrimaryUnaryExprContext):
        return self.visit(ctx.primary_expression())

    def visitParenExpr(self, ctx: SQLParser.ParenExprContext):
        return self.visit(ctx.expression())

    def visitScalarSubqueryExpr(self, ctx: SQLParser.ScalarSubqueryExprContext):
        return self.visit(ctx.select_statement())

    def visitExistsExpr(self, ctx: SQLParser.ExistsExprContext):
        return ExistsExpressionNode(self.visit(ctx.select_statement()))

    def visitCaseExpr(self, ctx: SQLParser.CaseExprContext):
        exprs = ctx.expression()
        whens = []
        end = len(exprs) - (1 if ctx.ELSE() else 0)
        for i in range(0, end, 2):
            condition = self.visit(exprs[i])
            result = self.visit(exprs[i + 1])
            whens.append(WhenClauseNode(condition, result))
        else_expr = self.visit(exprs[-1]) if ctx.ELSE() else None
        return CaseExpressionNode(whens, else_expr)

    def visitFunctionCallExpr(self, ctx: SQLParser.FunctionCallExprContext):
        return self.visit(ctx.function_call())

    def visitAtomExpr(self, ctx: SQLParser.AtomExprContext):
        return self.visit(ctx.atom())

    def visitFunction_call(self, ctx: SQLParser.Function_callContext):
        name = self._text_from_id(ctx.id_name())
        if ctx.STAR():
            args = [StarNode()]
        elif ctx.expression_list():
            args = self.visit(ctx.expression_list())
        else:
            args = []
        return FunctionCallNode(name, args)

    def visitAtom(self, ctx: SQLParser.AtomContext):
        if ctx.constant():
            return self.visit(ctx.constant())
        if ctx.table_name():
            return IdentifierNode(self._text_from_table(ctx.table_name()))
        return self.visit(ctx.variable())

    def visitConstant(self, ctx: SQLParser.ConstantContext):
        if ctx.INT():
            return LiteralNode(int(ctx.INT().getText()))
        if ctx.FLOAT():
            return LiteralNode(float(ctx.FLOAT().getText()))
        if ctx.STRING():
            return LiteralNode(ctx.STRING().getText().strip("'").replace("''", "'"))
        if ctx.NSTRING():
            return LiteralNode(ctx.NSTRING().getText())
        if ctx.TRUE():
            return LiteralNode(True)
        if ctx.FALSE():
            return LiteralNode(False)
        if ctx.NULL():
            return LiteralNode(None)
        return None

    def visitVariable(self, ctx: SQLParser.VariableContext):
        return VariableNode(ctx.getText())

    # Helpers ---------------------------------------------------------
    def visitTable_name(self, ctx: SQLParser.Table_nameContext):
        parts = [self.visit(idc) for idc in self._as_list(ctx.id_name())]
        return TableNode(parts)

    def visitId_name(self, ctx: SQLParser.Id_nameContext):
        return IdentifierNode(ctx.getText())

    def _text_from_id(self, ctx):
        return ctx.getText()

    def _text_from_table(self, ctx):
        return ctx.getText()

    def _as_list(self, value):
        if value is None:
            return []
        return value if isinstance(value, list) else [value]

    def _fold_left(self, nodes, operator):
        if not nodes:
            return None
        current = nodes[0]
        for nxt in nodes[1:]:
            current = BinaryExpressionNode(operator, current, nxt)
        return current

    def _fold_with_ops(self, nodes, ops):
        if not nodes:
            return None
        current = nodes[0]
        for op, nxt in zip(ops, nodes[1:]):
            current = BinaryExpressionNode(op, current, nxt)
        return current
