"""Simple AST printer that relies on node.print()."""

class ASTPrinter:
    def print(self, node, file=None):
        if node is None:
            print("🌳 AST: فارغ", file=file)
            return

        print("\n" + "🌳 " * 10, file=file)
        print("✨ AST (الشجرة المجردة للتركيب)", file=file)
        print("🌳 " * 10, file=file)

        if isinstance(node, list):
            for i, stmt in enumerate(node, start=1):
                print(f"\n📄 Statement {i}:", file=file)
                stmt.print(1)
        else:
            node.print(0)

        print("\n" + "─" * 80, file=file)
