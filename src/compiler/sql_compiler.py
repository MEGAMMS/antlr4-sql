from antlr4 import *
from src.antlr_generated.SQLLexer import SQLLexer
from src.antlr_generated.SQLParser import SQLParser
from grammar.AST.ast_builder import ASTBuilder

class SQLCompiler:
    @staticmethod
    def main():
        # مثال SQL (نفس الموجود في PDF)
        sql = """
        SELECT 
            foo, bar 
        FROM 
            mytable 
        WHERE 
            foo = 5
        ORDER BY 
            foo DESC;
        """

        print("===== SQL INPUT =====")
        print(sql.strip())
        print("=====================\n")

        # 1. Input stream
        input_stream = InputStream(sql)

        # 2. Lexer
        lexer = SQLLexer(input_stream)
        token_stream = CommonTokenStream(lexer)

        # 3. Parser
        parser = SQLParser(token_stream)
        tree = parser.sql_script()

        # 4. AST Builder (BaseVisitor)
        builder = ASTBuilder()
        ast = builder.visit(tree)

        # 5. Print AST
        print("===== AST =====")
        ast.print()
        print("================")


if __name__ == "__main__":
    SQLCompiler.main()
