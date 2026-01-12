#!/usr/bin/env bash
set -e

ANTLR_JAR="tools/antlr/antlr-4.13.2-complete.jar"
GRAMMAR_DIR="grammar"
OUT_DIR="src/antlr_generated"

mkdir -p "$OUT_DIR"

LEXER="$GRAMMAR_DIR/SQLLexer.g4"
PARSER="$GRAMMAR_DIR/SQLParser.g4"

FOUND=false

if [[ -f "$LEXER" ]]; then
  echo "Generating lexer from SQLLexer.g4"
  java -jar "$ANTLR_JAR" \
    -Dlanguage=Python3 \
    -visitor \
    -no-listener \
    "$LEXER" \
    -o "$OUT_DIR"
  FOUND=true
fi

if [[ -f "$PARSER" ]]; then
  echo "Generating parser from SQLParser.g4"
  java -jar "$ANTLR_JAR" \
    -Dlanguage=Python3 \
    -visitor \
    -no-listener \
    "$PARSER" \
    -o "$OUT_DIR"
  FOUND=true
fi

if [[ "$FOUND" = false ]]; then
  echo "❌ Error: No grammar files found."
  echo "Expected at least one of:"
  echo "  - grammar/SQLLexer.g4"
  echo "  - grammar/SQLParser.g4"
  exit 1
fi

# make it excutable "chmod +x scripts/generate_parser.sh"
# then run the script "./scripts/generate_parser.sh"