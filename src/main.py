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

if __name__ == "__main__":
    main()