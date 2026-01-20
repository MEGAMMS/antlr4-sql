import sys
import os

# إضافة المسارات
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

def main():
    print("🔧 مترجم SQL - الواجهة الرئيسية")
    print("=" * 60)
    
    from compiler.sql_compiler import SQLCompiler
    SQLCompiler.main()

if __name__ == "__main__":
    main()