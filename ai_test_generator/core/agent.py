from ai_test_generator.core.test_generator import generate_test_code
from ai_test_generator.core.extractor import extract_functions
import importlib.util
import os

def create_test_file(source_path):
    module_name = os.path.splitext(os.path.basename(source_path))[0]
    spec = importlib.util.spec_from_file_location(module_name, source_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    functions = extract_functions(source_path)

    test_lines = []
    for func in functions:
        test_code = generate_test_code(func, module, functions)
        test_lines.append(test_code)

    test_file_path = f"tests/test_{module_name}.py"
    with open(test_file_path, "w") as f:
        f.write("from application." + module_name + " import *\n")
        for line in test_lines:
            f.write(line)

    print(f"Test file created at: {test_file_path}")
