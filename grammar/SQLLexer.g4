lexer grammar SQLLexer;

@members {
def emitError(self, msg):
    listener = self.getErrorListenerDispatch()
    listener.syntaxError(self, None, self._tokenStartLine, self._tokenStartColumn, msg, None)

def nextToken(self):
    token = super().nextToken()
    if token.type == Token.EOF and self._mode == self.COMMENT:
        self.emitError("unterminated block comment")
        self.popMode()
    return token
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

// ========== Keywords (Explicit Definitions) =============

DECLARE : D E C L A R E ;
GO      : G O ;

CURSOR  : C U R S O R ;
OPEN    : O P E N ;
FETCH   : F E T C H ;
NEXT    : N E X T ;
CLOSE   : C L O S E ;
DEALLOCATE : D E A L L O C A T E ;
FOR     : F O R ;

TRUNCATE : T R U N C A T E;

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

PRIMARY : P R I M A R Y ;
KEY     : K E Y ;
ADD     : A D D ;
COLUMN  : C O L U M N ;
VIEW    : V I E W ;
PROCEDURE : P R O C E D U R E ;
USE     : U S E ;

JOIN  : J O I N ;
INNER : I N N E R ;
LEFT  : L E F T ;
ON    : O N ;

GROUP  : G R O U P ;
BY     : B Y ;
HAVING : H A V I N G ;

CLUSTERED : C L U S T E R E D;
NONCLUSTERED : N O N C L U S T E R E D;
CONSTRAINT : C O N S T R A I N T;
REFERENCES : R E F E R E N C E S;
UNIQUE : U N I Q U E;
CHECK : C H E C K;
FOREIGN : F O R E I G N;

ORDER : O R D E R ;
ASC   : A S C ;
DESC  : D E S C ;

NULL : N U L L ;
IS   : I S ;

UNION : U N I O N ;
BEGIN : B E G I N ;
END   : E N D ;
CASE  : C A S E ;
WHEN  : W H E N ;
THEN  : T H E N ;
ELSE  : E L S E ;
EXISTS: E X I S T S ;
IN    : I N ;
IF    : I F ;
TRY   : T R Y ;
CATCH : C A T C H ;
EXEC  : E X E C ;
PRINT : P R I N T ;
DEFAULT : D E F A U L T ;
IDENTITY: I D E N T I T Y ;
TOP   : T O P ;
OUTPUT: O U T P U T ;
WITH  : W I T H ;
OVER  : O V E R ;
PARTITION : P A R T I T I O N ;
RIGHT : R I G H T ;
FULL  : F U L L ;
CROSS : C R O S S ;
OUTER : O U T E R ;
BETWEEN : B E T W E E N ;
LIKE : L I K E ;

// ===== Operators =====
PLUS_ASSIGN    : '+=' ;
MINUS_ASSIGN   : '-=' ;
STAR_ASSIGN    : '*=' ;
SLASH_ASSIGN   : '/=' ;
PERCENT_ASSIGN : '%=' ;

GE  : '>=' ;
LE  : '<=' ;
NEQ : '!=' | '<>' ;
NOT_LESS    : '!<' ;
NOT_GREATER : '!>' ;
EQ  : '=' ;
GT  : '>' ;
LT  : '<' ;

PLUS  : '+' ;
MINUS : '-' ;
STAR  : '*' ;
SLASH : '/' ;
PERCENT : '%' ;
BIT_AND : '&' ;
BIT_OR  : '|' ;
BIT_XOR : '^' ;
BIT_NOT : '~' ;

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

// ===== Strings =====
NSTRING
  : [nN] '\'' ( '\'\'' | ~['] )* '\''
  ;

UNCLOSED_NSTRING_EOF
  : [nN] '\'' ( '\'\'' | ~['] )* EOF
    { self.emitError("unterminated string literal") }
    -> skip
  ;

STRING
  : '\'' ( '\'\'' | ~['] )* '\''
  ;

UNCLOSED_STRING_EOF
  : '\'' ( '\'\'' | ~['] )* EOF
    { self.emitError("unterminated string literal") }
    -> skip
  ;

// ===== Comments =====
LINE_COMMENT : '--' ~[\r\n]* -> skip ;
BLOCK_COMMENT_START : '/*' -> pushMode(COMMENT), skip ;

mode COMMENT; // wrong mode COMMENT;
  // BLOCK_COMMENT_END  : '*/' -> popMode, skip ;
  // COMMENT_TEXT        : .    -> skip ;
  NESTED_BLOCK_START : '/*' -> pushMode(COMMENT), skip ;
  BLOCK_COMMENT_END  : '*/' -> popMode, skip ;
  COMMENT_TEXT        : .    -> skip ;
  UNTERMINATED_BLOCK_COMMENT
    : EOF
      { self.emitError("unterminated block comment") }
      -> popMode, skip
    ;

mode DEFAULT_MODE;

// ===== BOOLEAN & LITERALS =====
TRUE  : T R U E ;
FALSE : F A L S E ;

HEX_LITERAL : '0' [xX] HEXDIGIT+ (LINE_CONT HEXDIGIT+)* ;

INVALID_HEX_LITERAL
  : '0' [xX] HEXDIGIT+ (LINE_CONT HEXDIGIT+)* [g-zG-Z_] [a-zA-Z0-9_]*
    { self.emitError("invalid hex literal") }
    -> skip
  ;

BIT_STRING  : '0' [bB] [01]+ (LINE_CONT [01]+)* ;

INVALID_BIT_STRING
  : '0' [bB] [01]+ (LINE_CONT [01]+)* [2-9a-zA-Z_] [a-zA-Z0-9_]*
    { self.emitError("invalid bit string") }
    -> skip
  ;

GLOBAL_VAR : '@@' [a-zA-Z_][a-zA-Z0-9_]* ;
LOCAL_VAR  : '@'  [a-zA-Z_][a-zA-Z0-9_]* ;
TEMP_ID    : '#' '#'? [a-zA-Z_][a-zA-Z0-9_]* ;

BRACKET_ID : '[' ( ']]' | ~[\]\r\n] )* ']' ;
DQUOTED_ID : '"' ( '""' | ~["\r\n] )* '"' ;

UNCLOSED_BRACKET_ID
  : '[' ~[\]\r\n]* (EOF | '\r'? '\n')
    { self.emitError("unterminated bracket identifier") }
    -> skip
  ;

// ===== Identifiers =====
// تم إزالة كود البايثون لتجنب التضارب مع البارسير
ID
  : [a-zA-Z_][a-zA-Z0-9_]*
  ;

// ===== Whitespace =====
WS : [ \t\r\n]+ -> skip ;

ERROR_CHAR
  : .
    { self.emitError(f"unexpected character: {self.text}") }
    -> skip
  ;
