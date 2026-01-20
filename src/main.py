import sys
import os
from antlr4.error.ErrorListener import ErrorListener  # <-- 1. استيراد ErrorListener

# ضبط المسارات
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from antlr4 import FileStream, CommonTokenStream
from src.antlr_generated.SQLLexer import SQLLexer
from src.antlr_generated.SQLParser import SQLParser
from tree_printer import print_parse_tree, print_full_tree, print_tree_text

# 2. إنشاء صنف بسيط لعد الأخطاء
class ErrorCounter(ErrorListener):
    def __init__(self):
        self.count = 0

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.count += 1

def main():
    if len(sys.argv) < 2:
        print("Usage: python src/main.py <file.sql>")
        sys.exit(1)

    input_file = sys.argv[1]
    
    print(f"Processing file: {input_file}...\n")

    # 1. مرحلة التحليل اللغوي (Lexing)
    input_stream = FileStream(input_file, encoding='utf-8')
    lexer = SQLLexer(input_stream)
    
    # 3. إضافة عداد الأخطاء إلى الليكسر
    error_counter = ErrorCounter()
    lexer.addErrorListener(error_counter)
    
    stream = CommonTokenStream(lexer)
    
    # إجبار الليكسر على قراءة الملف بالكامل الآن لاكتشاف الأخطاء
    stream.fill()

    # 4. التحقق من العداد بدلاً من الدالة غير الموجودة
    if error_counter.count > 0:
        print(f"\n❌ Lexer found {error_counter.count} errors. Parsing aborted.")
        sys.exit(1)

    # 2. مرحلة التحليل النحوي (Parsing)
    print("✅ Lexer finished successfully. Starting Parser...")
    parser = SQLParser(stream)
    tree = parser.sql_script() 

    # 3. التحقق من أخطاء البارسـر (هنا الدالة موجودة بشكل طبيعي)
    if parser.getNumberOfSyntaxErrors() > 0:
        print("❌ Parser found Syntax Errors!")
    else:
        print("✅ Parsed Successfully!")
        print(tree.toStringTree(recog=parser))
    

     
    # 3. طباعة Parse Tree
    print("\n" + "=" * 60)
    print("🌳 نتائج التحليل")
    print("=" * 60)
    
    # خيارات الطباعة
    if 1:
        print("\n1. شجرة مختصرة (عمق 4):")
        print_parse_tree(tree, parser, max_depth=4)
        
        print("\n2. عرض نصي محسن:")
        print_tree_text(tree, parser, max_width=100)
        
        # إذا أردت الشجرة كاملة (تحذير: قد تكون طويلة)
        # print("\n3. الشجرة الكاملة:")
        # print_full_tree(tree, parser)
    else:
        print("\n📊 Parse Tree (النسخة الأساسية):")
        print("=" * 60)
        tree_str = tree.toStringTree(recog=parser)
        # تقسيم النص الطويل
        max_line = 100
        for i in range(0, len(tree_str), max_line):
            print(tree_str[i:i+max_line])
        print("=" * 60)
    
    print(f"\n✅ تم تحليل {input_file} بنجاح!")


if __name__ == "__main__":
    main()