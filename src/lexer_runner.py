from antlr4 import FileStream, CommonTokenStream, Token
from antlr_generated.SQLLexer import SQLLexer # type: ignore

def tokenize_file(path: str) -> list[tuple[str, str, int, int]]:
    lexer = SQLLexer(FileStream(path, encoding="utf-8"))
    stream = CommonTokenStream(lexer)
    stream.fill()

    vocab = lexer.vocabulary
    out: list[tuple[str, str, int, int]] = []

    for t in stream.tokens:
        if t.type == Token.EOF:
            break
        name = vocab.getDisplayName(t.type).strip("'")
        out.append((name, t.text, t.line, t.column))

    return out

def print_tokens(path: str) -> None:
    tokens = tokenize_file(path)
    print("== TOKENS ==")
    for name, text, line, col in tokens:
        print(f"{name:12} text={text!r:25} line={line} col={col}")
