import ast

def extract_functions(file_path):
    with open(file_path, "r") as source:
        tree = ast.parse(source.read())

    function_names = []

    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            function_names.append("global", node.name)
        elif isinstance(node, ast.ClassDef):
            class_name = node.name
            for item in node.body:
                if isinstance(item, ast.FunctionDef) and item.name != "__init__":
                    
                    function_names.append((class_name, item.name))

    return function_names
