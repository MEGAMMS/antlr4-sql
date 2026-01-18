parser grammar SQLParser;

options { tokenVocab = SQLLexer; }

// ==========================================
// Root Rule
// ==========================================

root
    : sql_script EOF
    ;

sql_script
    : batch*
    ;

batch
    : (sql_statement SEMI?)+ (GO SEMI?)?   # StatementBatch
    | GO SEMI?                             # EmptyGo
    ;

// ==========================================
// SQL Statements
// ==========================================

sql_statement
    : ddl_statement
    | dml_statement
    | control_flow_statement
    | print_statement
    | declare_statement
    | set_statement
    | execute_statement    // <--- أضف هذا
    ;

ddl_statement
    : create_statement
    | alter_statement
    | drop_statement
    | truncate_statement
    | use_statement
    ;

dml_statement
    : select_statement
    | insert_statement
    | update_statement
    | delete_statement
    ;


// ==========================================
// DDL (Create, Alter, Drop)
// ==========================================

create_statement
    : CREATE TABLE table_name LPAREN column_def_list RPAREN
    ;

column_def_list
    : column_def (COMMA column_def)*
    ;

column_def
    : id_name data_type (column_constraint)*
    ;

data_type
    : id_name (LPAREN (INT | id_name) (COMMA INT)? RPAREN)? 
    ;

column_constraint
    : NOT NULL
    | NULL
    | PRIMARY KEY
    | DEFAULT expression
    | IDENTITY (LPAREN INT COMMA INT RPAREN)?
    ;

alter_statement
    : ALTER TABLE table_name ADD column_def              # AlterAdd
    | ALTER TABLE table_name DROP COLUMN id_name         # AlterDrop
    | ALTER TABLE table_name ALTER COLUMN column_def     # AlterModify
    ;

drop_statement
    : DROP (TABLE | VIEW | PROCEDURE) table_name
    ;

truncate_statement
    : TRUNCATE TABLE table_name
    ;

use_statement
    : USE id_name  // Fixed: Removed quotes 'USE' -> USE
    ;

// ==========================================
// DML (Select, Insert, Update, Delete)
// ==========================================

// --- SELECT ---
// --- SELECT ---
select_statement
    : with_expression? 
      SELECT (DISTINCT)? (TOP INT)? 
      select_list 
      (
        FROM table_source 
        (join_part)*
        (WHERE expression)?
        (GROUP BY group_list)?
        (HAVING expression)?
      )? 
      (ORDER BY order_list)?
    ;
// تم التعديل: القائمة أصبحت تحتوي على select_item
select_list
    : STAR
    | select_item (COMMA select_item)*
    ;

// قاعدة جديدة: تحدد ما يمكن كتابته داخل SELECT
select_item
    : variable (EQ | PLUS_ASSIGN | MINUS_ASSIGN | STAR_ASSIGN | SLASH_ASSIGN | PERCENT_ASSIGN) expression  # SelectVarAssignment
    | id_name EQ expression                                                                                # SelectAliasAssignment
    | expression (AS? id_name)?                                                                            # SelectExpression
    ;

table_source
    : table_name (AS? id_name)?
    | LPAREN select_statement RPAREN (AS? id_name)?
    ;

join_part
    : (INNER | LEFT | RIGHT | FULL | CROSS)? (OUTER)? JOIN table_source ON expression
    ;

group_list
    : expression (COMMA expression)*
    ;

order_list
    : expression (ASC | DESC)? (COMMA expression (ASC | DESC)?)*
    ;

insert_statement
    : INSERT (INTO)? table_name (LPAREN column_list RPAREN)? 
      (
        VALUES expression_list_parens (COMMA expression_list_parens)* // <--- تم التعديل
      | select_statement
      )
    ;

// قاعدة مساعدة جديدة للأقواس
expression_list_parens
    : LPAREN expression_list RPAREN
    ;

column_list
    : id_name (COMMA id_name)*
    ;

expression_list
    : expression (COMMA expression)*
    ;

// --- UPDATE ---
update_statement
    : UPDATE table_name 
      SET assignment_list 
      (WHERE expression)?
    ;

assignment_list
    : assignment (COMMA assignment)*
    ;

assignment
    : id_name EQ expression
    | id_name (PLUS_ASSIGN | MINUS_ASSIGN | STAR_ASSIGN | SLASH_ASSIGN) expression
    ;

// --- DELETE ---
delete_statement
    : DELETE (FROM)? table_name (WHERE expression)?
    ;

// ==========================================
// Variables (DECLARE)
// ==========================================

declare_statement
    : DECLARE declare_list
    ;

declare_list
    : declare_item (COMMA declare_item)*
    ;

declare_item
    : LOCAL_VAR (AS)? data_type (EQ expression)?
    ;

// ==========================================
// Set Variables
// ==========================================

set_statement
    : SET variable (EQ | PLUS_ASSIGN | MINUS_ASSIGN | STAR_ASSIGN | SLASH_ASSIGN | PERCENT_ASSIGN) expression
    ;

// ==========================================
// Control Flow & Others
// ==========================================

control_flow_statement
    // التعديل: وضعنا BEGIN TRY في البداية لتكون لها الأولوية
    : BEGIN TRY (sql_statement SEMI?)* END TRY BEGIN CATCH (sql_statement SEMI?)* END CATCH
    | BEGIN (sql_statement SEMI?)* END
    | IF expression sql_statement (ELSE sql_statement)?
    ;

print_statement
    : PRINT expression
    ;
execute_statement
    // التعديل: دعمنا المتغيرات كاسم للإجراء، ودعمنا استقبال القيمة العائدة
    : EXEC (variable EQ)? (table_name | variable) (expression (COMMA expression)*)?
    ;

with_expression
    : WITH id_name AS LPAREN select_statement RPAREN
    ;

// ==========================================
// Expressions
// ==========================================

expression
    : LPAREN expression RPAREN                       # ParenExpr
    | NOT expression                                 # NotExpr
    | expression (STAR | SLASH | PERCENT) expression # MultiplicativeExpr
    | expression (PLUS | MINUS) expression           # AdditiveExpr
    // تمت إضافة BETWEEN هنا
    | expression (NOT)? BETWEEN expression AND expression # BetweenExpr
    | expression (EQ | NEQ | GT | LT | GE | LE) expression # ComparisonExpr
    | expression (NOT)? LIKE expression                    # LikeExpr
    | expression (AND | OR) expression               # LogicalExpr
    | expression IS NULL                             # IsNullExpr
    | expression IS NOT NULL                         # IsNotNullExpr
    | expression (NOT)? IN LPAREN (expression_list | select_statement) RPAREN # InExpr
    | EXISTS LPAREN select_statement RPAREN          # ExistsExpr
    // تمت إضافة هذا السطر لدعم (SELECT ...) كقيمة
    | LPAREN select_statement RPAREN                 # ScalarSubqueryExpr 
    | CASE (WHEN expression THEN expression)+ (ELSE expression)? END # CaseExpr
    | function_call                                  # FunctionCallExpr
    | atom                                           # AtomExpr
    ;

function_call
    : id_name LPAREN (expression_list)? RPAREN
    ;

atom
    : table_name
    | constant
    | variable
    ;

// ==========================================
// Identifiers & Tables
// ==========================================

table_name
    : id_name (DOT id_name)*
    ;

id_name
    : ID
    | BRACKET_ID
    | DQUOTED_ID
    | STRING
    ;

constant
    : INT
    | FLOAT
    | STRING
    | NSTRING
    | TRUE
    | FALSE
    | NULL
    ;

variable
    : GLOBAL_VAR
    | LOCAL_VAR
    ;