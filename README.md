# antlr4-sql

A SQL parser and Abstract Syntax Tree (AST) builder for T-SQL (Transact-SQL) using ANTLR4. This project parses SQL scripts, generates parse trees, and builds structured AST representations suitable for analysis, transformation, or code generation.

## Features

### Lexical Analysis
Tokenizes T-SQL code with support for:
- **Variables**: `@var`, `@@GLOBAL_VAR`
- **String literals**: standard and Unicode (`N'...'`)
- **Identifiers**: quoted (`[...]`), double-quoted (`"..."`), and regular
- **Numeric literals**: integers, floats, hex (`0x...`), binary (`0b...`)
- **Comments**: line (`--`) and nested block (`/* ... */`)
- All major SQL keywords and operators

### Syntax Parsing
Comprehensive grammar supporting:
- **DDL**: `CREATE TABLE`, `ALTER TABLE`, `DROP`, `TRUNCATE`, `USE`
- **DML**: `SELECT`, `INSERT`, `UPDATE`, `DELETE` with CTEs (`WITH`)
- **Joins**: `INNER`, `LEFT`, `RIGHT`, `FULL`, `CROSS` (with `OUTER`)
- **Control flow**: `IF/ELSE`, `BEGIN/END`, `TRY/CATCH`
- **Variables**: `DECLARE`, `SET`, variable assignments in `SELECT`
- **Cursors**: `DECLARE CURSOR`, `OPEN`, `FETCH`, `CLOSE`, `DEALLOCATE`
- **Procedures**: `EXEC`/`EXECUTE` statements
- **Complex expressions**: arithmetic, logical, `CASE`, `BETWEEN`, `IN`, `LIKE`, `EXISTS`

### AST Generation
Builds a structured Abstract Syntax Tree with:
- Typed nodes for statements, expressions, and literals
- Visitor pattern support for tree traversal
- Graphviz DOT export for visualization

### Error Handling
Detailed error reporting with line and column numbers

## Prerequisites

- **Python 3.14+**
- **Java JDK 17+** (required to generate the parser from grammar files)

> Java is only needed to run ANTLR's code generation. Once the parser is generated, Java is not required at runtime.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd antlr4-sql
   ```
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Generate the parser (requires Java):
   Linux/macOS:
   ```bash
   chmod +x scripts/generate_parser.sh
   ./scripts/generate_parser.sh
   ```
   Windows (PowerShell):
   ```bash
   .\scripts\generate_parser.ps1
   ```
   The ANTLR JAR is included in ```tools/antlr/antlr-4.13.2-complete.jar.```

## Usage
Command Line Interface
Run the compiler on SQL files:
```bash
python src/main.py examples/test4.sql
```
Options:

--show-tokens: Display lexer tokens
--show-parse-tree: Print the parse tree
--ast-dot <path>: Export AST as Graphviz DOT file

Example:
```bash
python src/main.py examples/test6.sql --show-tokens --ast-dot ast.dot
```
View the AST graph:
```bash
dot -Tpng ast.dot -o ast.png
```
## Programmatic Usage
```python
from sql_compiler import SQLCompiler

# Parse a SQL file
ast = SQLCompiler.run_file("path/to/script.sql")

# Parse a SQL string
sql = "SELECT * FROM users WHERE id = 1;"
ast = SQLCompiler.run_string(sql, label="query")

# Generate DOT graph
from sql_ast.graph import ast_to_dot
dot_code = ast_to_dot(ast)
```
## AST Structure
The AST is composed of typed nodes inheriting from ASTNode:
```python
from sql_ast import (
    SelectNode,           # SELECT statements
    InsertStatement,      # INSERT statements
    UpdateStatement,      # UPDATE statements
    CreateTableNode,      # CREATE TABLE
    BinaryExpressionNode, # Binary operations (AND, OR, +, -, etc.)
    FunctionCallNode,     # Function calls
    VariableNode,         # Variables
    LiteralNode,          # Constants
    # ... and many more
)
```
Each node provides:

label(): Human-readable label
children(): List of child nodes
Node-specific attributes (e.g., SelectNode.where_clause)
## Project Structure
```
antlr4-sql/
├── grammar/              # ANTLR4 grammar files
│   ├── SQLLexer.g4      # Lexer rules
│   └── SQLParser.g4     # Parser rules
├── src/
│   ├── antlr_generated/ # Generated lexer/parser (auto-created)
│   ├── sql_ast/         # AST node definitions
│   │   ├── base.py      # Base AST node classes
│   │   ├── expressions.py  # Expression nodes
│   │   ├── statements.py   # Statement nodes
│   │   ├── builder.py   # AST builder (visitor)
│   │   └── graph.py     # DOT graph generation
│   ├── main.py          # CLI entry point
│   ├── sql_compiler.py  # Compiler orchestration
│   └── tools.py         # Utilities (tree printer, etc.)
├── examples/            # Sample SQL files
├── tests/               # Test suite
├── scripts/             # Parser generation scripts
└── tools/antlr/        # ANTLR JAR file
```
## Testing
Run the test suite:
``` pytest ```
Tests validate parsing of example SQL files in the examples/ directory.

## Grammar Details
The project defines a T-SQL compatible grammar with two main files:

SQLLexer.g4: Tokenizes SQL into keywords, identifiers, literals, operators, and comments
SQLParser.g4: Defines the syntactic structure of SQL statements
Key features:

Case-insensitive keywords
Support for bracketed [id] and double-quoted "id" identifiers
Temporary table names (#temp)
Nested block comments
Line continuation with backslash (\)
Compound assignment operators (+=, -=, etc.)

Examples
Simple SELECT
```
SELECT id, name 
FROM users 
WHERE status = 'active'
ORDER BY name ASC;
```
Complex Query with CTE
```
WITH ActiveUsers AS (
    SELECT * FROM users WHERE status = 'active'
)
SELECT u.name, COUNT(o.id) as order_count
FROM ActiveUsers u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.name
HAVING COUNT(o.id) > 5;
```
Variable Assignment
```sql
DECLARE @count INT;
SELECT @count = COUNT(*) FROM users;
PRINT @count;
```
See the examples/ directory for more comprehensive samples.
## Development
Modifying the Grammar
1. Edit grammar/SQLLexer.g4 or grammar/SQLParser.g4
2. Regenerate the parser:
   ```
   ./scripts/generate_parser.sh  # or .ps1 on Windows
   ```
3. Update AST builder in src/sql_ast/builder.py if needed
Adding AST Nodes
1. Define the node in src/sql_ast/statements.py or expressions.py
2. Update ASTBuilder visitor methods in builder.py
3. Export from src/sql_ast/__init__.py
## Limitations
- Focuses on T-SQL syntax (Microsoft SQL Server)
- Some advanced SQL Server features may not be fully supported
- Error recovery is basic (parsing stops on first syntax error)
## License
This project is provided as-is for educational and research purposes.

## Contributing
Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Submit a pull request
## Acknowledgments
- Built with [ANTLR4](https://www.antlr.org/?spm=a2ty_o01.29997173.0.0.15295171equsyr) by Terence Parr
- Parser generation uses ANTLR v4.13.2
- Inspired by T-SQL language specification
