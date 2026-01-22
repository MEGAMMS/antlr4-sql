#!/usr/bin/env bash
set -e

ANTLR_JAR="tools/antlr/antlr-4.13.2-complete.jar"
GRAMMAR_DIR="grammar"
OUT_ROOT="src/antlr_generated"

rm -rf "$OUT_ROOT"
mkdir -p "$OUT_ROOT"
touch "$OUT_ROOT/__init__.py"

echo "Generating lexer from SQLLexer.g4"
java -jar "$ANTLR_JAR" \
  -Xexact-output-dir \
  -Dlanguage=Python3 \
  -visitor \
  -no-listener \
  "$GRAMMAR_DIR/SQLLexer.g4" \
  -o "$OUT_ROOT"

# ANTLR drops tokens next to the grammar (.antlr). Copy them where the parser step can find them.
if [ -f "$GRAMMAR_DIR/.antlr/SQLLexer.tokens" ]; then
  cp "$GRAMMAR_DIR/.antlr/SQLLexer.tokens" "$OUT_ROOT/SQLLexer.tokens"
  cp "$GRAMMAR_DIR/.antlr/SQLLexer.tokens" "$GRAMMAR_DIR/SQLLexer.tokens"
elif [ -f "$OUT_ROOT/SQLLexer.tokens" ]; then
  cp "$OUT_ROOT/SQLLexer.tokens" "$GRAMMAR_DIR/SQLLexer.tokens"
fi

echo "Generating parser from SQLParser.g4"
java -jar "$ANTLR_JAR" \
  -Xexact-output-dir \
  -Dlanguage=Python3 \
  -visitor \
  -no-listener \
  -lib "$OUT_ROOT" \
  "$GRAMMAR_DIR/SQLParser.g4" \
  -o "$OUT_ROOT"



# make it excutable "chmod +x scripts/generate_parser.sh"
# then run the script "./scripts/generate_parser.sh"
