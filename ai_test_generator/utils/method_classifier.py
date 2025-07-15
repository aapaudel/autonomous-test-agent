

import ast

def is_mutator_node(node):
    if not isinstance(node, ast.FunctionDef):
        return False
    for stmt in ast.walk(node):
        if isinstance(stmt, ast.Assign):
            for target in stmt.targets:
                if isinstance(target, ast.Attribute) and isinstance(target.value, ast.Name) and target.value.id == 'self':
                    return True
    return False

def is_accessor_node(node):
    if not isinstance(node, ast.FunctionDef):
        return False
    for stmt in ast.walk(node):
        if isinstance(stmt, ast.Return):
            return True
    return False
