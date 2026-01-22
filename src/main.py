import argparse
import os
import sys
from pathlib import Path

# Ensure src/ and project root are on the import path for CLI usage
ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
for path in (ROOT, SRC):
    str_path = str(path)
    if str_path not in sys.path:
        sys.path.insert(0, str_path)


def _build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="SQL compiler CLI")
    parser.add_argument(
        "files",
        nargs="*",
        help="SQL files to compile (default: built-in sample)",
    )
    parser.add_argument(
        "--show-tokens",
        action="store_true",
        default=False,
        help="Print lexer tokens",
    )
    parser.add_argument(
        "--show-parse-tree",
        action="store_true",
        default=False,
        help="Print parse tree",
    )
    parser.add_argument(
        "--ast-dot",
        help="Write AST graphviz DOT to the given path (for the last processed input)",
    )
    return parser


def main():
    from sql_compiler import SQLCompiler

    parser = _build_arg_parser()
    args = parser.parse_args()

    ast_result = None
    if args.files:
        for path in args.files:
            ast_result = SQLCompiler.run_file(
                path,
                show_parse_tree=args.show_parse_tree,
                show_tokens=args.show_tokens,
            )
    else:
        sample_sql = "SELECT 1 + 1 AS result;"
        ast_result = SQLCompiler.run_string(
            sample_sql,
            label="inline sample",
            show_parse_tree=args.show_parse_tree,
            show_tokens=args.show_tokens,
        )

    if args.ast_dot and ast_result is not None:
        from sql_ast.graph import ast_to_dot
        out_path = Path(args.ast_dot)
        out_path.write_text(ast_to_dot(ast_result), encoding="utf-8")
        print(f"Wrote AST DOT to {out_path}")


if __name__ == "__main__":
    main()
