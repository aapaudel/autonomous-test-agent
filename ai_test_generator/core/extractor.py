import ast
import textwrap

def extract_functions(file_path):
    with open(file_path, "r") as source_file:
        source_code = source_file.read()
        tree = ast.parse(source_code)

    functions = []
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            code = ast.get_source_segment(source_code, node)
            functions.append({"source": textwrap.dedent(code)})
        elif isinstance(node, ast.ClassDef):
            for item in node.body:
                if isinstance(item, ast.FunctionDef) and item.name != "__init__":
                    code = ast.get_source_segment(source_code, item)
                    functions.append({"source": textwrap.dedent(code)})

    return functions

