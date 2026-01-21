import sys
import os

# إضافة المسارات
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
sys.path.insert(0, current_dir)

def main():
    from compiler.sql_compiler import SQLCompiler
    args = sys.argv[1:]
    if not args:
        default_file = os.path.join(parent_dir, "examples", "test6.sql")
        args = [default_file]

    for path in args:
        SQLCompiler.run_file(path, show_parse_tree=False, show_tokens=True)

if __name__ == "__main__":
    main()
