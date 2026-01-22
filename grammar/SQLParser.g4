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
    | cursor_statement 
    | control_flow_statement
    | print_statement
    | declare_statement
    | set_statement
    | execute_statement
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
    | with_expression insert_statement
    | with_expression update_statement
    | with_expression delete_statement
    ;


// ==========================================
// DDL (Create, Alter, Drop)
// ==========================================

create_statement
    : CREATE TABLE table_name LPAREN table_element_list RPAREN  // column_def_list renamed to table_element_list
    ;

// Table elements can be columns or table constraints
table_element_list
    : table_element (COMMA table_element)*
    ;

table_element
    : column_def
    | table_constraint
    ;

column_def
    : id_name data_type (column_constraint)*
    ;

// Supports standalone table constraints such as CONSTRAINT PK ...
table_constraint
    : (CONSTRAINT id_name)? (PRIMARY KEY | UNIQUE) (CLUSTERED | NONCLUSTERED)? LPAREN column_list RPAREN
    | (CONSTRAINT id_name)? FOREIGN KEY LPAREN column_list RPAREN REFERENCES table_name LPAREN column_list RPAREN
    | (CONSTRAINT id_name)? CHECK LPAREN expression RPAREN
    ;

data_type
    : id_name (LPAREN (INT | id_name) (COMMA INT)? RPAREN)? 
    ;

column_constraint
    : NOT NULL
    | NULL
    | PRIMARY KEY (CLUSTERED | NONCLUSTERED)?  // CLUSTERED allowed here too
    | UNIQUE 
    | DEFAULT expression
    | IDENTITY (LPAREN INT COMMA INT RPAREN)?
    | REFERENCES table_name LPAREN id_name RPAREN // Allow inline foreign keys
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
// The select list now contains select_item entries
select_list
    : STAR
    | select_item (COMMA select_item)*
    ;

// Defines what can appear inside a SELECT list
select_item
    : variable (EQ | PLUS_ASSIGN | MINUS_ASSIGN | STAR_ASSIGN | SLASH_ASSIGN | PERCENT_ASSIGN) expression  # SelectVarAssignment
    | id_name EQ expression                                                                                # SelectAliasAssignment
    | expression (AS? alias_name)?                                                                         # SelectExpression
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
        VALUES expression_list_parens (COMMA expression_list_parens)* // Updated to accept parenthesized lists
      | select_statement
      )
    ;

// Helper rule for parenthesized value lists
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
    : DECLARE (cursor_declare_statement | declare_list)
    ;

cursor_declare_statement
    : id_name CURSOR FOR select_statement
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

cursor_statement
    : open_cursor_statement
    | fetch_cursor_statement
    | close_cursor_statement
    | deallocate_cursor_statement
    ;

open_cursor_statement
    : OPEN id_name
    ;

fetch_cursor_statement
    : FETCH (NEXT)? FROM id_name (INTO variable_list)?
    ;

variable_list
    : variable (COMMA variable)*
    ;

close_cursor_statement
    : CLOSE id_name
    ;

deallocate_cursor_statement
    : DEALLOCATE id_name
    ;


// ==========================================
// Control Flow & Others
// ==========================================

control_flow_statement
    : try_catch
    | begin_block
    | if_statement
    ;

try_catch
    : BEGIN TRY block END TRY BEGIN CATCH block END CATCH
    ;

begin_block
    : BEGIN block END
    ;

block
    : (sql_statement SEMI?)*
    ;

if_statement
    : IF expression sql_statement SEMI? (ELSE sql_statement SEMI?)?
    ;

print_statement
    : PRINT expression
    ;
execute_statement
    // Allow variables as procedure names and capturing return value
    : EXEC (variable EQ)? (table_name | variable) (expression (COMMA expression)*)?
    ;

with_expression
    : WITH cte_definition (COMMA cte_definition)*
    ;

cte_definition
    : id_name (LPAREN column_list RPAREN)? AS LPAREN select_statement RPAREN
    ;

// ==========================================
// Expressions
// ==========================================

expression
    : logical_or_expression
    ;

logical_or_expression
    : logical_and_expression (OR logical_and_expression)*   # LogicalOrExpr
    ;

logical_and_expression
    : not_expression (AND not_expression)*                  # LogicalAndExpr
    ;

not_expression
    : NOT not_expression                                    # NotExpr
    | comparison_expression                                 # PredicateExpr
    ;

comparison_expression
    : additive_expression (EQ | NEQ | GT | LT | GE | LE) additive_expression        # ComparisonExpr
    | additive_expression (NOT)? BETWEEN additive_expression AND additive_expression # BetweenExpr
    | additive_expression (NOT)? IN LPAREN (expression_list | select_statement) RPAREN # InExpr
    | additive_expression (NOT)? LIKE additive_expression                            # LikeExpr
    | additive_expression IS NOT? NULL                                               # IsNullExpr
    | additive_expression                                                            # ValueExpr
    ;

additive_expression
    : multiplicative_expression ((PLUS | MINUS) multiplicative_expression)*          # AdditiveExpr
    ;

multiplicative_expression
    : unary_expression ((STAR | SLASH | PERCENT | BIT_XOR) unary_expression)*        # MultiplicativeExpr
    ;

unary_expression
    : (PLUS | MINUS) unary_expression                                                # UnaryExpr
    | primary_expression                                                             # PrimaryUnaryExpr
    ;

primary_expression
    : LPAREN expression RPAREN                                                       # ParenExpr
    | LPAREN select_statement RPAREN                                                 # ScalarSubqueryExpr
    | EXISTS LPAREN select_statement RPAREN                                          # ExistsExpr
    | CASE (WHEN expression THEN expression)+ (ELSE expression)? END                 # CaseExpr
    | function_call                                                                  # FunctionCallExpr
    | atom                                                                           # AtomExpr
    ;

function_call
    : id_name LPAREN (STAR | expression_list)? RPAREN
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
    | TEMP_ID
    ;

alias_name
    : id_name
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
