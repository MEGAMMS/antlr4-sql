$ANTLR_JAR = "tools/antlr/antlr-4.13.2-complete.jar"
$GRAMMAR_DIR = "grammar"
$OUT_DIR = "src/antlr_generated"

New-Item -ItemType Directory -Force -Path $OUT_DIR | Out-Null

$Lexer = Join-Path $GRAMMAR_DIR "SQLLexer.g4"
$Parser = Join-Path $GRAMMAR_DIR "SQLParser.g4"

$Found = $false

if (Test-Path $Lexer) {
  Write-Host "Generating lexer from SQLLexer.g4"
  java -jar $ANTLR_JAR `
    -Dlanguage=Python3 `
    -visitor `
    -no-listener `
    $Lexer `
    -Xexact-output-dir `
    -o $OUT_DIR
  $Found = $true
}

if (Test-Path $Parser) {
  Write-Host "Generating parser from SQLParser.g4"
  java -jar $ANTLR_JAR `
    -Dlanguage=Python3 `
    -visitor `
    -no-listener `
    $Parser `
    -Xexact-output-dir `
    # -lib "$OUT_DIR/grammar" `
    -lib $OUT_DIR `
    -o $OUT_DIR 
  $Found = $true
}

if (-not $Found) {
  Write-Error "No grammar files found. Expected SQLLexer.g4 and/or SQLParser.g4"
  exit 1
}

# run the script ".\scripts\generate_parser.ps1"
