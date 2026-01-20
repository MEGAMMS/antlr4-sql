import sys
import os
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from antlr_generated.SQLLexer import SQLLexer
from antlr_generated.SQLParser import SQLParser
from grammar.AST.ast_builder import ASTBuilder

class ErrorListenerWithCount(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errors = []
    
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_msg = f"line error :{line}:{column} - {msg}"
        self.errors.append(error_msg)

class SQLCompiler:

    
    @staticmethod
    def main():
        input_arg = sys.argv[1]
        
        if os.path.exists(input_arg) and input_arg.endswith('.sql'):
            print(f"📂 read file: {input_arg}")
            try:
                with open(input_arg, 'r', encoding='utf-8') as f:
                    sql_input = f.read()
            except Exception as e:
                print(f"❌ error {e}")
                sys.exit(1)
        else:
            sql_input = input_arg
        
        print(f"\n sql query:")
        print("-" * 40)
        print(sql_input)
        print("-" * 40)
        
        input_stream = InputStream(sql_input)
        
        print("\n🔤 lexer phase:")
        lexer = SQLLexer(input_stream)
        lexer_error_listener = ErrorListenerWithCount()
        lexer.removeErrorListeners()
        lexer.addErrorListener(lexer_error_listener)
        
        stream = CommonTokenStream(lexer)
        stream.fill()
        
        if not lexer_error_listener.errors:
            print("✅ success")
            print(f"  Tokens: {len(stream.tokens)}")
        else:
            print("❌ error ")
            for error in lexer_error_listener.errors:
                print(f"   - {error}")
            sys.exit(1)
        
        print("\n🔍 parser phase")
        parser = SQLParser(stream)
        parser_error_listener = ErrorListenerWithCount()
        parser.removeErrorListeners()
        parser.addErrorListener(parser_error_listener)
        
        # بناء Parse Tree
        tree = parser.sql_script()
        
        if parser_error_listener.errors:
            print("❌ error")
            for error in parser_error_listener.errors:
                print(f"   - {error}")
            sys.exit(1)
        
        print("✅ Parse Tree")
        
        print("\n✨ AST phase")
        
        visitor = ASTBuilder()
        
        ast = visitor.visit(tree)
        
        if ast is None:
            print("⚠️ empty versitor")
            sys.exit(1)
        
        print("✅ baseVisitor!")
        
        print("\n🌳AST...")
        print("="*60)
        
        SQLCompiler._print_ast(ast)
        
    
    @staticmethod
    def _print_ast(node, indent=0, is_last=True):
        if node is None:
            return
        
        # إنشاء البادئة
        prefix = ""
        if indent > 0:
            prefix = "│   " * (indent - 1)
            prefix += "└── " if is_last else "├── "
        
        node_type = node.__class__.__name__
        
        info = ""
        if hasattr(node, '__dict__'):
            simple_fields = {}
            for key, value in node.__dict__.items():
                if not key.startswith('_'):
                    if isinstance(value, (str, int, float, bool)) or value is None:
                        simple_fields[key] = value
            
            if simple_fields:
                info = " " + str(simple_fields)
        
        print(f"{prefix}{node_type}{info}")
        
        if hasattr(node, '__dict__'):
            child_items = []
            for key, value in node.__dict__.items():
                if not key.startswith('_'):
                    if isinstance(value, list) and value:
                        child_items.extend([(f"{key}[{i}]", item) for i, item in enumerate(value)])
                    elif hasattr(value, '__class__') and value.__class__.__name__ != 'type':
                        child_items.append((key, value))
            
            for i, (child_name, child_value) in enumerate(child_items):
                is_last_child = (i == len(child_items) - 1)
                
                child_prefix = "│   " * indent
                child_prefix += "    " if is_last else "│   "
                print(f"{child_prefix}├── [{child_name}]")
                
                SQLCompiler._print_ast(child_value, indent + 2, is_last_child)

if __name__ == "__main__":
    SQLCompiler.main()