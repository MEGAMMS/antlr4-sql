from antlr4 import FileStream, CommonTokenStream, Token
from antlr_generated.grammar.SQLLexer import SQLLexer


def _get_vocab(lexer: SQLLexer):
    if hasattr(lexer, "getVocabulary"):
        return lexer.getVocabulary()
    if hasattr(SQLLexer, "VOCABULARY"):
        return SQLLexer.VOCABULARY
    if hasattr(lexer, "_vocabulary"):
        return lexer._vocabulary
    return None


def tokenize_file(path: str) -> list[tuple[str, str, int, int]]:
    lexer = SQLLexer(FileStream(path, encoding="utf-8"))
    stream = CommonTokenStream(lexer)
    stream.fill()

    vocab = _get_vocab(lexer)
    out: list[tuple[str, str, int, int]] = []

    for t in stream.tokens:
        if t.type == Token.EOF:
            break

        if vocab:
            name = vocab.getDisplayName(t.type).strip("'")
        else:
            # fallback بسيط (نادر)
            name = str(t.type)

        out.append((name, t.text, t.line, t.column))

    return out


def print_tokens(path: str) -> None:
    print("== TOKENS ==")
    for name, text, line, col in tokenize_file(path):
        print(f"{name:15} text={text!r:25} line={line} col={col}")
