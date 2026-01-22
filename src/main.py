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
        help="SQL files to compile (default: examples/test6.sql)",
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
    return parser


def main():
    from compiler.sql_compiler import SQLCompiler

    parser = _build_arg_parser()
    args = parser.parse_args()

    paths = args.files or [ROOT / "examples" / "test6.sql"]
    for path in paths:
        SQLCompiler.run_file(
            path,
            show_parse_tree=args.show_parse_tree,
            show_tokens=args.show_tokens,
        )


if __name__ == "__main__":
    main()
