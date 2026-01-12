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

fragment DIGIT : [0-9];
fragment HEXDIGIT : [0-9a-fA-F];

// =======================


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
