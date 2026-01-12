lexer grammar SQLLexer;

tokens { KEYWORD } 

@members {
  RESERVED = {
    "SELECT","FROM","WHERE","AND","OR","NOT","AS","DISTINCT","DECLARE",
    "INSERT","INTO","VALUES","UPDATE","SET","DELETE",
    "CREATE","TABLE","ALTER","DROP",
    "JOIN","INNER","LEFT","ON",
    "GROUP","BY","HAVING","ORDER","ASC","DESC","NULL","IS","GO"
  }
}

// ===== Fragments =====
fragment A : [aA];
fragment B : [bB];
fragment C : [cC];
fragment D : [dD];
fragment E : [eE];
fragment F : [fF];
fragment G : [gG];
fragment H : [hH];
fragment I : [iI];
fragment J : [jJ];
fragment K : [kK];
fragment L : [lL];
fragment M : [mM];
fragment N : [nN];
fragment O : [oO];
fragment P : [pP];
fragment Q : [qQ];
fragment R : [rR];
fragment S : [sS];
fragment T : [tT];
fragment U : [uU];
fragment V : [vV];
fragment W : [wW];
fragment X : [xX];
fragment Y : [yY];
fragment Z : [zZ];

fragment LINE_CONT : '\\' '\r'? '\n' [ \t]* ;

fragment DIGIT : [0-9];
fragment HEXDIGIT : [0-9a-fA-F];

// ==========Keywords=============


DECLARE : D E C L A R E ;
GO      : G O ;


SELECT   : S E L E C T ;
FROM     : F R O M ;
WHERE    : W H E R E ;
AND      : A N D ;
OR       : O R ;
NOT      : N O T ;
AS       : A S ;
DISTINCT : D I S T I N C T ;

INSERT : I N S E R T ;
INTO   : I N T O ;
VALUES : V A L U E S ;

UPDATE : U P D A T E ;
SET    : S E T ;
DELETE : D E L E T E ;

CREATE : C R E A T E ;
TABLE  : T A B L E ;
ALTER  : A L T E R ;
DROP   : D R O P ;

JOIN  : J O I N ;
INNER : I N N E R ;
LEFT  : L E F T ;
ON    : O N ;

GROUP  : G R O U P ;
BY     : B Y ;
HAVING : H A V I N G ;

ORDER : O R D E R ;
ASC   : A S C ;
DESC  : D E S C ;

NULL : N U L L ;
IS   : I S ;

UNION : U N I O N ;

// ===== Operators =====
GE  : '>=' ;
LE  : '<=' ;
NEQ : '!=' | '<>' ;
EQ  : '=' ;
GT  : '>' ;
LT  : '<' ;

PLUS  : '+' ;
MINUS : '-' ;
STAR  : '*' ;
SLASH : '/' ;

COMMA  : ',' ;
DOT    : '.' ;
SEMI   : ';' ;
LPAREN : '(' ;
RPAREN : ')' ;

// ===== Numbers =====

FLOAT
  : DIGIT+ '.' DIGIT*
  | '.' DIGIT+
  ;

INT : DIGIT+ ;


// ===== Strings=====
STRING : '\'' ( '\'\'' | LINE_CONT | ~['\\\r\n] | '\\' . )* '\'' ;


// ===== Comments =====
LINE_COMMENT : '--' ~[\r\n]* -> skip ;
BLOCK_COMMENT_START : '/*' -> pushMode(COMMENT), skip ;

mode COMMENT;
  NESTED_BLOCK_START : '/*' -> pushMode(COMMENT), skip ;
  BLOCK_COMMENT_END  : '*/' -> popMode, skip ;
  COMMENT_TEXT       : .    -> skip ;

mode DEFAULT_MODE;

// ===== BOOLEAN =====
TRUE  : T R U E ;
FALSE : F A L S E ;


HEX_LITERAL : '0' [xX] HEXDIGIT+ (LINE_CONT HEXDIGIT+)* ;
BIT_STRING  : '0' [bB] [01]+ (LINE_CONT [01]+)* ;

GLOBAL_VAR : '@@' [a-zA-Z_][a-zA-Z0-9_]* ;
LOCAL_VAR  : '@'  [a-zA-Z_][a-zA-Z0-9_]* ;

// ===== Identifiers =====
ID
  : [a-zA-Z_][a-zA-Z0-9_]*
    {
if self.text.upper() in self.RESERVED:
  self.type = self.KEYWORD
    }
  ;

// ===== Whitespace =====
WS : [ \t\r\n]+ -> skip ;




