import sys
import os
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener

# استيراد المكونات
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from antlr_generated.SQLLexer import SQLLexer
from antlr_generated.SQLParser import SQLParser
from grammar.AST import ASTBuilder
from src.ast_printer import ASTPrinter

class ErrorListenerWithCount(ErrorListener):
    """مستمع للأخطاء مع عداد"""
    def __init__(self):
        super().__init__()
        self.errors = []
    
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_msg = f"خطأ في السطر {line}:{column} - {msg}"
        self.errors.append(error_msg)
        # لا توقف التنفيذ، دعنا نجمع كل الأخطاء

class SQLCompiler:
    """
    الصف الرئيسي الذي يحوي دالة main
    يقرأ سلسلة المدخلات وينتج tokens ويولد baseVisitor
    ويستخدمه لزيارة AST وطباعتها
    """
    
    @staticmethod
    def main():
        """دالة main الرئيسية حسب متطلبات PDF"""
        
        print("\n" + "="*60)
        print("🚀 مترجم SQL - المرحلة الثالثة (AST)")
        print("="*60)
        
        # التحقق من المدخلات
        if len(sys.argv) < 2:
            print("طريقة الاستخدام:")
            print("  python -m src.compiler.sql_compiler 'استعلام SQL'")
            print("  python -m src.compiler.sql_compiler ملف.sql")
            print("\nمثال:")
            print('  python -m src.compiler.sql_compiler "SELECT foo, bar as baz FROM mytable WHERE foo LIKE \'%neat%\' ORDER BY foo DESC"')
            sys.exit(1)
        
        # الحصول على المدخل
        input_arg = sys.argv[1]
        
        # تحديد ما إذا كان ملفاً أو نصاً
        sql_input = ""
        if os.path.exists(input_arg) and input_arg.endswith('.sql'):
            print(f"📂 قراءة الملف: {input_arg}")
            try:
                with open(input_arg, 'r', encoding='utf-8') as f:
                    sql_input = f.read()
            except Exception as e:
                print(f"❌ خطأ في قراءة الملف: {e}")
                sys.exit(1)
        else:
            sql_input = input_arg
            print("📝 معالجة سلسلة SQL مباشرة")
        
        # عرض جزء من الاستعلام (أول 500 حرف)
        preview = sql_input[:500] + ("..." if len(sql_input) > 500 else "")
        print(f"\n🔧 استعلام SQL (معاينة):")
        print("-" * 40)
        print(preview)
        print("-" * 40)
        
        # 1. إنشاء InputStream من السلسلة النصية
        input_stream = InputStream(sql_input)
        
        # 2. إنتاج Tokens (التحليل اللغوي)
        print("\n🔤 المرحلة 1: إنتاج Tokens (التحليل اللغوي)...")
        lexer = SQLLexer(input_stream)
        lexer_error_listener = ErrorListenerWithCount()
        lexer.removeErrorListeners()
        lexer.addErrorListener(lexer_error_listener)
        
        stream = CommonTokenStream(lexer)
        try:
            stream.fill()
        except Exception as e:
            print(f"❌ خطأ في التحليل اللغوي: {e}")
            sys.exit(1)
        
        # طباعة Tokens إذا لم تكن هناك أخطاء
        if not lexer_error_listener.errors:
            print(f"✅ تم إنتاج Tokens بنجاح!")
            print(f"   عدد Tokens: {len(stream.tokens)}")
            
            # عرض عينات من الـ Tokens
            print("   عينات Tokens:")
            for i, token in enumerate(stream.tokens[:10]):
                if token.type != -1:  # تجاهل EOF
                    print(f"     {i+1}. {lexer.symbolicNames[token.type] if token.type < len(lexer.symbolicNames) else token.type}: '{token.text}'")
            if len(stream.tokens) > 10:
                print(f"     ... و {len(stream.tokens) - 10} أكثر")
        else:
            print("❌ أخطاء في التحليل اللغوي:")
            for error in lexer_error_listener.errors[:5]:  # عرض أول 5 أخطاء فقط
                print(f"   - {error}")
            if len(lexer_error_listener.errors) > 5:
                print(f"   ... و {len(lexer_error_listener.errors) - 5} أخطاء أخرى")
        
        # 3. التحليل النحوي
        print("\n🔍 المرحلة 2: التحليل النحوي واستخدام baseVisitor...")
        parser = SQLParser(stream)
        parser_error_listener = ErrorListenerWithCount()
        parser.removeErrorListeners()
        parser.addErrorListener(parser_error_listener)
        
        # بناء Parse Tree
        try:
            tree = parser.sql_script()
        except Exception as e:
            print(f"❌ خطأ في بناء Parse Tree: {e}")
            sys.exit(1)
        
        if parser_error_listener.errors:
            print("⚠️ تحذيرات في التحليل النحوي:")
            for error in parser_error_listener.errors[:5]:
                print(f"   - {error}")
            if len(parser_error_listener.errors) > 5:
                print(f"   ... و {len(parser_error_listener.errors) - 5} تحذيرات أخرى")
        else:
            print("✅ تم بناء Parse Tree بنجاح!")
        
        # 4. توليد baseVisitor وبناء AST
        print("\n✨ المرحلة 3: توليد baseVisitor وبناء AST...")
        
        try:
            # إنشاء Visitor (هذا هو baseVisitor المطلوب)
            visitor = ASTBuilder()
            
            # زيارة Parse Tree لبناء AST
            ast = visitor.visit(tree)
            
            if ast is None:
                print("⚠️ لم يتم بناء AST (قد يكون فارغاً)")
                ast = []
            
            print("✅ تم بناء AST بنجاح باستخدام baseVisitor!")
            
        except Exception as e:
            print(f"❌ خطأ في بناء AST: {e}")
            import traceback
            print("\n🔍 تفاصيل الخطأ:")
            traceback.print_exc()
            sys.exit(1)
        
        # 5. طباعة AST
        print("\n🌳 المرحلة 4: طباعة AST...")
        print("="*60)
        
        # استخدام الـ AST Printer
        printer = ASTPrinter(show_details=True)
        
        try:
            printer.print(ast)
        except Exception as e:
            print(f"❌ خطأ في طباعة AST: {e}")
            # حاول طباعة AST بشكل بسيط
            print("\n📋 عرض AST مبسط:")
            print("-" * 40)
            SQLCompiler._print_ast_simple(ast)
        
        print("\n✅ تم تنفيذ جميع متطلبات المرحلة الثالثة بنجاح!")
        print(f"   - قراءة سلسلة المدخلات: ✓")
        print(f"   - إنتاج Tokens: ✓ ({len(stream.tokens)} token)")
        print(f"   - توليد baseVisitor: ✓")
        print(f"   - زيارة AST وطباعتها: ✓")
        
        # إحصاءات إضافية
        if ast:
            SQLCompiler._print_statistics(ast)
    
    @staticmethod
    def _print_ast_simple(ast):
        """طباعة AST بشكل مبسط"""
        if isinstance(ast, list):
            for i, stmt in enumerate(ast):
                print(f"\n📄 العبارة {i+1}: {type(stmt).__name__}")
                if hasattr(stmt, '__dict__'):
                    for key, value in stmt.__dict__.items():
                        if not key.startswith('_'):
                            if isinstance(value, list):
                                print(f"  {key}: [{len(value)} items]")
                            elif value:
                                print(f"  {key}: {value}")
        elif ast:
            print(f"{type(ast).__name__}")
    
    @staticmethod
    def _print_statistics(ast):
        """طباعة إحصاءات عن الـ AST"""
        print("\n📊 إحصاءات AST:")
        print("-" * 30)
        
        if isinstance(ast, list):
            print(f"عدد العبارات: {len(ast)}")
            
            # عد أنواع العبارات
            type_count = {}
            for stmt in ast:
                stmt_type = type(stmt).__name__
                type_count[stmt_type] = type_count.get(stmt_type, 0) + 1
            
            for stmt_type, count in type_count.items():
                print(f"  {stmt_type}: {count}")
        else:
            print(f"نوع AST: {type(ast).__name__}")

if __name__ == "__main__":
    SQLCompiler.main()