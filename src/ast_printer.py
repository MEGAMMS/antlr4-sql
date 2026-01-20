# ast_printer.py

class ASTPrinter:
    
    def __init__(self, indent_size=2):
        self.indent_size = indent_size
    
    def print(self, node, indent=0):
        if node is None:
            return
        
        if isinstance(node, list):
            for item in node:
                self.print(item, indent)
            return
        
        # طباعة العقدة الحالية
        node_str = self._node_to_string(node)
        print(" " * indent + node_str)
        
        # طباعة الأطفال
        if hasattr(node, '__dict__'):
            for key, value in node.__dict__.items():
                if key.startswith('_') or value is None:
                    continue
                
                if isinstance(value, list):
                    if value and not isinstance(value[0], (int, float, str, bool)):
                        print(" " * (indent + self.indent_size) + f"{key}:")
                        for item in value:
                            self.print(item, indent + self.indent_size * 2)
                elif isinstance(value, (int, float, str, bool)):
                    print(" " * (indent + self.indent_size) + f"{key}: {value}")
                else:
                    print(" " * (indent + self.indent_size) + f"{key}:")
                    self.print(value, indent + self.indent_size * 2)
    
    def _node_to_string(self, node):
        class_name = node.__class__.__name__
        
        if isinstance(node, SelectStatement):
            return f"📄 SelectStatement"
        elif isinstance(node, CreateTableStatement):
            return f"🆕 CreateTable: {node.table_name}"
        elif isinstance(node, InsertStatement):
            return f"📝 InsertInto: {node.table_name}"
        elif isinstance(node, UpdateStatement):
            return f"✏️ Update: {node.table_name}"
        elif isinstance(node, DeleteStatement):
            return f"🗑️ DeleteFrom: {node.table_name}"
        elif isinstance(node, ColumnDefinition):
            return f"📊 Column: {node.name} ({node.data_type.name})"
        elif isinstance(node, BinaryExpression):
            return f"🔧 BinaryOp: {node.operator}"
        elif isinstance(node, Literal):
            value_str = f"'{node.value}'" if node.type == 'STRING' else str(node.value)
            return f"📌 Literal: {value_str}"
        elif isinstance(node, ColumnReference):
            table_prefix = f"{node.table}." if node.table else ""
            return f"📍 ColumnRef: {table_prefix}{node.name}"
        
        return f"📦 {class_name}"