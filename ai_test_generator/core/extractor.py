import ast
import textwrap

def extract_functions(file_path):
    with open(file_path, "r") as source_file:
        source_code = source_file.read()
        tree = ast.parse(source_code)

    functions = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name != "__init__":
            code = ast.get_source_segment(source_code, node)
            if code:
                functions.append({"source": textwrap.dedent(code)})

    return functions
