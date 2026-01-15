from antlr4 import FileStream, CommonTokenStream, Token
from grammar.SQLLexer import SQLLexer
from antlr4.error.ErrorListener import ErrorListener

class CollectingErrorListener(ErrorListener):
    def __init__(self):
        self.errors: list[str] = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f"line {line}:{column} {msg}")


def token_type_name(lexer: SQLLexer, ttype: int) -> str:
    if ttype == Token.EOF:
        return "EOF"

    # 1) symbolicNames (مثل SELECT, ID, STRING...)
    try:
        sym = lexer.symbolicNames[ttype]
        if sym and not sym.startswith("T__"):
            return sym
    except Exception:
        pass

    # 2) literals أو T__x -> خذ الاسم من Vocabulary
    try:
        vocab = lexer.getVocabulary()
        name = vocab.getDisplayName(ttype)
        return name.strip("'")  # "+", "(", ...
    except Exception:
        return str(ttype)


def tokenize_file(path: str, strict: bool = False):
    lexer = SQLLexer(FileStream(path, encoding="utf-8"))

    err = CollectingErrorListener()
    lexer.removeErrorListeners()
    lexer.addErrorListener(err)

    stream = CommonTokenStream(lexer)
    stream.fill()

    if strict and err.errors:
        # وقف على أول Lexical error
        raise SyntaxError(err.errors[0])

    tokens = []
    for t in stream.tokens:
        if t.type == Token.EOF:
            break
        tokens.append(t)

    return tokens, err.errors, lexer


def print_tokens(path: str, strict: bool = False) -> None:
    tokens, errors, lexer = tokenize_file(path, strict=strict)

    if errors:
        print("== LEXER ERRORS ==")
        for e in errors:
            print(e)
        print()

    print("== TOKENS ==")
    print(f"{'#':>4}  {'TYPE':>4}  {'NAME':<18}  {'TEXT':<30}  {'POS':<10}")
    print("-" * 78)

    for i, t in enumerate(tokens, start=1):
        name = token_type_name(lexer, t.type)
        text = repr(t.text)  # يبين \n و \r بشكل واضح
        pos = f"{t.line}:{t.column}"
        print(f"{i:>4}  {t.type:>4}  {name:<18}  {text:<30}  {pos:<10}")
