#!/usr/bin/env bash
set -e

ANTLR_JAR="tools/antlr/antlr-4.13.2-complete.jar"
OUT_DIR="src/antlr_generated"
GRAMMAR_DIR="grammar"

rm -rf "$OUT_DIR"
mkdir -p "$OUT_DIR"


cd "$GRAMMAR_DIR"
java -jar "../$ANTLR_JAR" \
    -Dlanguage=Python3 \
    -visitor \
    -no-listener \
    SQLLexer.g4 SQLParser.g4 \
    -o "../$OUT_DIR"
cd ..


# make it excutable "chmod +x scripts/generate_parser.sh"
# then run the script "./scripts/generate_parser.sh"