#!/usr/bin/env bash
set -e

ANTLR_JAR="tools/antlr/antlr-4.13.2-complete.jar"
GRAMMAR_DIR="grammar"
OUT_DIR="src/antlr_generated"

rm -rf "$OUT_DIR"
mkdir -p "$OUT_DIR"

echo "Generating lexer from SQLLexer.g4"
java -jar "$ANTLR_JAR" \
  -Dlanguage=Python3 \
  -visitor \
  -no-listener \
  "$GRAMMAR_DIR/SQLLexer.g4" \
  -o "$OUT_DIR"

echo "Generating parser from SQLParser.g4"
java -jar "$ANTLR_JAR" \
  -Dlanguage=Python3 \
  -visitor \
  -no-listener \
  -lib "$OUT_DIR/grammar" \
  "$GRAMMAR_DIR/SQLParser.g4" \
  -o "$OUT_DIR"



# make it excutable "chmod +x scripts/generate_parser.sh"
# then run the script "./scripts/generate_parser.sh"