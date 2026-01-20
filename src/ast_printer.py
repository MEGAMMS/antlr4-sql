

import sys
import os

# إضافة المسار للوصول إلى grammar/AST
sys.path.append(os.path.join(os.path.dirname(__file__), '../grammar/AST'))

try:
    from grammar.AST.ast_nodes import *
except ImportError:
    print("⚠️ تحذير: لم يتم العثور على ast_nodes")
    ASTNode = object

class ASTPrinter:
    """طابعة الـ AST بشكل هرمي"""
    
    def __init__(self, show_details=True):
        self.show_details = show_details
    
    def print(self, node, file=None):
        """طباعة AST"""
        if node is None:
            print("🌳 AST: فارغ", file=file)
            return
        
        print("\n" + "🌳 " * 10, file=file)
        print("✨ AST (الشجرة المجردة للتركيب)", file=file)
        print("🌳 " * 10, file=file)
        
        self._print_node(node, 0, file=file)
        
        print("─" * 80, file=file)
    
    def _print_node(self, node, indent=0, is_last=True, file=None):
        """طباعة عقدة مع الأطفال"""
        if node is None:
            return
        
        # طباعة العقدة الحالية
        prefix = self._get_prefix(indent, is_last)
        node_str = self._node_to_string(node)
        print(f"{prefix}{node_str}", file=file)
        
        # طباعة الأطفال
        if isinstance(node, list):
            for i, child in enumerate(node):
                child_is_last = (i == len(node) - 1)
                self._print_node(child, indent + 1, child_is_last, file)
        elif hasattr(node, '__dict__'):
            children = []
            for key, value in node.__dict__.items():
                if not key.startswith('_'):
                    if isinstance(value, list) and value:
                        children.extend(value)
                    elif value and hasattr(value, '__class__'):
                        children.append(value)
            
            for i, child in enumerate(children):
                child_is_last = (i == len(children) - 1)
                self._print_node(child, indent + 1, child_is_last, file)
    
    def _get_prefix(self, indent, is_last):
        """إنشاء البادئة الهرمية"""
        if indent == 0:
            return ""
        
        prefix = "│   " * (indent - 1)
        prefix += "└── " if is_last else "├── "
        return prefix
    
    def _node_to_string(self, node):
        """تحويل العقدة إلى سلسلة نصية"""
        if node is None:
            return "None"
        
        node_type = node.__class__.__name__
        
        # معلومات إضافية حسب نوع العقدة
        info_parts = []
        
        if isinstance(node, SelectStatement):
            info_parts.append(f"SELECT")
            if node.distinct:
                info_parts.append("DISTINCT")
            if node.top:
                info_parts.append(f"TOP {node.top}")
        
        elif isinstance(node, CreateTableStatement):
            info_parts.append(f"CREATE TABLE {node.table_name}")
        
        elif isinstance(node, ColumnDefinition):
            info_parts.append(f"Column: {node.name}")
            if node.data_type:
                info_parts.append(f"Type: {node.data_type.name}")
        
        elif isinstance(node, Literal):
            value_str = f"'{node.value}'" if node.type == 'STRING' else str(node.value)
            info_parts.append(f"Value: {value_str}")
        
        elif isinstance(node, ColumnReference):
            table_prefix = f"{node.table}." if node.table else ""
            info_parts.append(f"Column: {table_prefix}{node.name}")
        
        elif isinstance(node, VariableReference):
            info_parts.append(f"Variable: {node.name}")
        
        info = f" ({', '.join(info_parts)})" if info_parts else ""
        return f"{node_type}{info}"