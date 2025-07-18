import os
import ast
from ai_test_generator.utils.watcher import ChangeWatcher
from ai_test_generator.core.extractor import extract_functions
from ai_test_generator.models.prompt_templates import TEST_PROMPT_TEMPLATE
from ai_test_generator.models.startcoder_wrapper import ModelWrapper


def extract_existing_test_names(test_file_path):
    """
    Parses the test file and returns a set of existing test function names.
    """
    if not os.path.exists(test_file_path):
        return set()

    with open(test_file_path, 'r') as f:
        tree = ast.parse(f.read(), filename=test_file_path)

    return {node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)}


def generate_tests_for_file(file_path, output_dir):
    """
    Generate tests for a single Python file and save to the output directory.
    Smart merge: avoids regenerating existing test cases.
    """
    print(f"\nScanning file: {file_path}")
    model = ModelWrapper()
    functions = extract_functions(file_path)
    print(f"Found {len(functions)} functions")

    if not functions:
        return

    test_file_name = f"test_{os.path.basename(file_path)}"
    test_file_path = os.path.join(output_dir, test_file_name)

    os.makedirs(output_dir, exist_ok=True)
    existing_tests = extract_existing_test_names(test_file_path)
    print(f"Writing to test file: {test_file_path}")

    with open(test_file_path, 'a') as f:
        if os.stat(test_file_path).st_size == 0:
            f.write("import pytest\n\n")

        for func in functions:
            source_code = func['source'] if isinstance(func, dict) else func
            prompt = TEST_PROMPT_TEMPLATE.format(function_code=source_code)
            test_code = model.generate(prompt)
            print(f"\n Prompt:\n{prompt}\n")
            print(f" Generated test:\n{test_code}\n")
            test_func_name = get_test_function_name(test_code)

            if test_func_name and test_func_name not in existing_tests:
                f.write(test_code + "\n\n")
            elif not test_func_name:
                f.write("#Could not generate valid test function for:\n")
                f.write(f"# {source_code}\n\n")


def get_test_function_name(test_code):
    """
    Extracts the first function name from a test code snippet.
    """
    try:
        tree = ast.parse(test_code)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                return node.name
    except Exception:
        return None


def generate_tests_for_changed_files(source_dir, output_dir):
    """
    Generate tests only for Python files that have changed since last run.
    """
    watcher = ChangeWatcher(watch_path=source_dir)
    changed_files = watcher.get_changed_files()

    if not changed_files:
        print("No changes detected.")
        return

    print(f"Detected changes in: {changed_files}")

    for file_path in changed_files:
        generate_tests_for_file(file_path, output_dir)

    watcher.save_cache()
    print("Test generation complete.")


def generate_tests_for_all_files(source_dir, output_dir):
    """
    Generate tests for all Python files (excluding test files) in a directory.
    """
    print("Generating tests for all Python files...")
    for dirpath, _, files in os.walk(source_dir):
        for file_name in files:
            if file_name.endswith(".py") and not file_name.startswith("test_"):
                file_path = os.path.join(dirpath, file_name)
                generate_tests_for_file(file_path, output_dir)
    print("Full test generation complete.")
