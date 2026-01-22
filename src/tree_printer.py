
from antlr4.tree.Tree import TerminalNodeImpl, ErrorNodeImpl
from antlr4 import ParserRuleContext, Token

class TreePrinter:
    def __init__(self, parser, show_tokens=True):
        self.parser = parser
        self.show_tokens = show_tokens
    
    def print_tree(self, node, indent=0, max_depth=None, is_last=True):
        if max_depth is not None and indent >= max_depth:
            self._print_indented("└─ ...", indent, is_last)
            return
        
        prefix = "│   " * (indent - 1) if indent > 0 else ""
        if indent > 0:
            prefix += "└── " if is_last else "├── "
        
        if isinstance(node, TerminalNodeImpl):
            if not self.show_tokens:
                return
            symbol = node.getSymbol()
            token_type = symbol.type
            
            if token_type == Token.EOF:
                token_name = "EOF"
            elif hasattr(self.parser, 'symbolicNames') and token_type < len(self.parser.symbolicNames):
                token_name = self.parser.symbolicNames[token_type]
                if not token_name:
                    token_name = f"<{token_type}>"
            else:
                token_name = f"<{token_type}>"
            
            text = symbol.text.replace('\n', '\\n').replace('\r', '\\r')
            print(f"{prefix}{token_name}: '{text}'")
        
        elif isinstance(node, ParserRuleContext):
            rule_name = self._get_rule_name(node)
            
            print(f"{prefix}[{rule_name}]")
            
            if hasattr(node, 'children') and node.children:
                child_count = len(node.children)
                for i, child in enumerate(node.children):
                    child_is_last = (i == child_count - 1)
                    self.print_tree(child, indent + 1, max_depth, child_is_last)
        
        elif isinstance(node, ErrorNodeImpl):
            print(f"{prefix}⚠ ERROR: {node}")
        
        else:
            print(f"{prefix}{type(node).__name__}")
    
    def _print_indented(self, text, indent, is_last):
        prefix = "│   " * (indent - 1) if indent > 0 else ""
        if indent > 0:
            prefix += "└── " if is_last else "├── "
        print(f"{prefix}{text}")
    
    def _get_rule_name(self, ctx):
        if hasattr(ctx, 'getRuleIndex') and hasattr(self.parser, 'ruleNames'):
            rule_index = ctx.getRuleIndex()
            if rule_index < len(self.parser.ruleNames):
                return self.parser.ruleNames[rule_index]
        return type(ctx).__name__

def print_parse_tree(tree, parser, max_depth=5):
    print("\n" + "🌳 " * 10)
    print("PARSE TREE")
    print("🌳 " * 10)
    printer = TreePrinter(parser, show_tokens=True)
    printer.print_tree(tree, max_depth=max_depth)
    print("─" * 80)

def print_full_tree(tree, parser):
    print("\n" + "🌳 " * 10)
    print("complex PARSE TREE (full)")
    print("🌳 " * 10)
    printer = TreePrinter(parser, show_tokens=True)
    printer.print_tree(tree)
    print("─" * 80)

def print_ast_view(tree, parser):
    print("\n" + "✨ " * 10)
    print("✨ AST VIEW (without tokens:)")
    print("✨ " * 10)
    printer = TreePrinter(parser, show_tokens=False)
    printer.print_tree(tree, max_depth=10)
    print("─" * 80)