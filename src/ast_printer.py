"""
طابعة AST - معدلة لدعم الأنواع الجديدة
"""

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
        
        if isinstance(node, list):
            for i, item in enumerate(node):
                print(f"\n📄 العبارة {i+1}:", file=file)
                print("-" * 40, file=file)
                self._print_node(item, 0, True, file)
        else:
            self._print_node(node, 0, True, file)
        
        print("\n" + "─" * 80, file=file)
    
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
            children = self._get_node_children(node)
            
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
    
    def _get_node_children(self, node):
        """الحصول على أطفال العقدة"""
        children = []
        
        if not hasattr(node, '__dict__'):
            return children
        
        # الحقول التي تعتبر أطفالاً
        child_fields = []
        
        if isinstance(node, SelectStatement):
            child_fields = [
                ('select_list', node.select_list),
                ('from_clause', node.from_clause),
                ('where_clause', node.where_clause),
                ('group_by', node.group_by),
                ('having_clause', node.having_clause),
                ('order_by', node.order_by),
            ]
            if hasattr(node, 'joins'):
                child_fields.append(('joins', node.joins))
                
        elif isinstance(node, CreateTableStatement):
            child_fields = [
                ('columns', node.columns),
                ('constraints', node.constraints),
            ]
        elif isinstance(node, InsertStatement):
            child_fields = [
                ('columns', node.columns),
                ('values', node.values),
                ('select_query', node.select_query),
            ]
        elif isinstance(node, UpdateStatement):
            child_fields = [
                ('assignments', node.assignments),
                ('where_clause', node.where_clause),
            ]
        elif isinstance(node, DeleteStatement):
            child_fields = [
                ('where_clause', node.where_clause),
            ]
        elif isinstance(node, ColumnDefinition):
            child_fields = [
                ('data_type', node.data_type),
                ('constraints', node.constraints),
            ]
        elif isinstance(node, BinaryExpression):
            child_fields = [
                ('left', node.left),
                ('right', node.right),
            ]
        elif isinstance(node, FunctionCall):
            child_fields = [
                ('arguments', node.arguments),
            ]
        elif isinstance(node, SelectItem):
            child_fields = [
                ('expression', node.expression),
            ]
        elif isinstance(node, DeclareStatement):
            child_fields = [
                ('variables', node.variables),
            ]
        
        # جمع الأطفال من الحقول
        for field_name, field_value in child_fields:
            if field_value:
                if isinstance(field_value, list):
                    children.extend(field_value)
                else:
                    children.append(field_value)
        
        return children
    
    def _node_to_string(self, node):
        """تحويل العقدة إلى سلسلة نصية"""
        if node is None:
            return "None"
        
        node_type = node.__class__.__name__
        
        # معلومات إضافية حسب نوع العقدة
        info_parts = []
        
        if isinstance(node, SelectStatement):
            info_parts.append("SELECT")
            if hasattr(node, 'distinct') and node.distinct:
                info_parts.append("DISTINCT")
            if hasattr(node, 'top') and node.top:
                info_parts.append(f"TOP {node.top}")
        
        elif isinstance(node, CreateTableStatement):
            info_parts.append(f"CREATE TABLE {node.table_name}")
        
        elif isinstance(node, InsertStatement):
            info_parts.append(f"INSERT INTO {node.table_name}")
        
        elif isinstance(node, UpdateStatement):
            info_parts.append(f"UPDATE {node.table_name}")
        
        elif isinstance(node, DeleteStatement):
            info_parts.append(f"DELETE FROM {node.table_name}")
        
        elif isinstance(node, ColumnDefinition):
            info_parts.append(f"Column: {node.name}")
            if node.data_type:
                params_str = ""
                if node.data_type.params:
                    params_str = f"({', '.join(map(str, node.data_type.params))})"
                info_parts.append(f"Type: {node.data_type.name}{params_str}")
        
        elif isinstance(node, DataType):
            params_str = ""
            if node.params:
                params_str = f"({', '.join(map(str, node.params))})"
            info_parts.append(f"{node.name}{params_str}")
        
        elif isinstance(node, Literal):
            value_str = f"'{node.value}'" if node.type in ['STRING', 'NSTRING'] else str(node.value)
            info_parts.append(f"Value: {value_str}")
        
        elif isinstance(node, ColumnReference):
            table_prefix = f"{node.table}." if node.table else ""
            info_parts.append(f"Column: {table_prefix}{node.name}")
        
        elif isinstance(node, VariableReference):
            info_parts.append(f"Variable: {node.name}")
        
        elif isinstance(node, FunctionCall):
            info_parts.append(f"Function: {node.name}")
        
        elif isinstance(node, BinaryExpression):
            info_parts.append(f"Operator: {node.operator}")
        
        elif isinstance(node, SelectItem):
            if node.alias:
                info_parts.append(f"Alias: {node.alias}")
        
        elif isinstance(node, UseStatement):
            info_parts.append(f"USE {node.database}")
        
        elif isinstance(node, PrintStatement):
            info_parts.append("PRINT")
        
        elif isinstance(node, DeclareStatement):
            info_parts.append(f"DECLARE {len(node.variables)} variables")
        
        elif isinstance(node, SetStatement):
            info_parts.append(f"SET {node.variable} {node.operator}")
        
        elif isinstance(node, IfStatement):
            info_parts.append("IF")
        
        info = f" ({', '.join(info_parts)})" if info_parts else ""
        return f"{node_type}{info}"