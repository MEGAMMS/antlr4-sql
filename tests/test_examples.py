import contextlib
import io
from pathlib import Path

import pytest

# Skip tests cleanly if ANTLR outputs are missing
try:
    import src.antlr_generated.SQLLexer  # noqa: F401
except ModuleNotFoundError:  # pragma: no cover
    pytestmark = pytest.mark.skip(reason="ANTLR output missing; run ./scripts/generate_parser.sh first")

from sql_compiler import SQLCompiler
from sql_ast.graph import ast_to_dot


EXAMPLES_DIR = Path(__file__).resolve().parents[1] / "examples"


def _run_file(path: Path, show_tokens: bool = False):
    """Run the SQL compiler on a file, capturing stdout noise."""
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        return SQLCompiler.run_file(str(path), show_tokens=show_tokens)


@pytest.mark.parametrize("filename", ["test4.sql", "test5.sql", "test6.sql", "test7.sql", "test8.sql", "test9.sql"])
def test_examples_parse_success(filename):
    ast = _run_file(EXAMPLES_DIR / filename, show_tokens=False)
    assert ast is not None


@pytest.mark.parametrize("filename", ["test.sql", "test2.sql", "test3.sql"])
def test_examples_known_errors(filename):
    ast = _run_file(EXAMPLES_DIR / filename, show_tokens=False)
    assert ast is None
