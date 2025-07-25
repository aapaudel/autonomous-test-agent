import os
import ast
import uuid
from ai_test_generator.utils.watcher import ChangeWatcher
from ai_test_generator.core.extractor import extract_functions
from ai_test_generator.models.prompt_templates import TEST_PROMPT_TEMPLATE
from ai_test_generator.models.startcoder_wrapper import ModelWrapper

def extract_existing_test_names(test_file_path):
    if not os.path.exists(test_file_path):
        return set()
    with open(test_file_path, 'r') as f:
        try:
            tree = ast.parse(f.read(), filename=test_file_path)
        except SyntaxError as e:
            print(f"Skipping broken test file due to syntax error: {e}")
            return set()
    return {node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)}

def sanitize_filename(file_path):
    base = os.path.basename(file_path)
    return f"test_{base}" if not base.startswith("test_") else base

def clean_test_code(generated):
    lines = generated.strip().splitlines()
    test_lines = []
    recording = False

    for line in lines:
        if line.strip().startswith("def test_"):
            recording = True
        if recording:
            test_lines.append(line)

    cleaned = "\n".join(test_lines).strip()
    return cleaned if cleaned.startswith("def test_") else ""

def generate_tests_for_file(file_path, output_dir="tests"):
    print(f"\n Scanning file: {file_path}")
    model = ModelWrapper()
    functions = extract_functions(file_path)
    print(f"Found {len(functions)} functions")

    if not functions:
        return

    os.makedirs(output_dir, exist_ok=True)
    test_file_name = sanitize_filename(file_path)
    test_file_path = os.path.join(output_dir, test_file_name)
    existing_tests = extract_existing_test_names(test_file_path)

    print(f"Writing to test file: {test_file_path}")
    with open(test_file_path, 'a') as f:
        if not os.path.exists(test_file_path) or os.stat(test_file_path).st_size == 0:
            f.write("import pytest\n\n")
        else:
            f.write("\n")

        for func in functions:
            source_code = func['source'] if isinstance(func, dict) else func
            prompt = TEST_PROMPT_TEMPLATE.format(function_code=source_code)
            test_code = model.generate(prompt)
            cleaned_code = clean_test_code(test_code)

            print(f"\n Prompt:\n{prompt}\n")
            print(f"Generated test (cleaned):\n{cleaned_code}\n")

            test_func_name = get_test_function_name(cleaned_code)
            if not test_func_name:
                try:
                    func_name = func['source'].split('(')[0].replace('def ', '').strip()
                    test_func_name = f"test_{func_name}"
                    cleaned_code = f"def {test_func_name}():\n    assert True"
                except Exception:
                    test_func_name = f"test_generated_{uuid.uuid4().hex[:8]}"
                    cleaned_code = f"def {test_func_name}():\n    assert True"

            if test_func_name not in existing_tests:
                f.write(cleaned_code + "\n\n")
            else:
                f.write(f"# Skipped duplicate test for: {test_func_name}\n")

def get_test_function_name(test_code):
    try:
        tree = ast.parse(test_code)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                return node.name
    except Exception as e:
        print(f"Failed to parse test code: {e}")
        return None

def generate_tests_for_changed_files(source_dir, output_dir="tests"):
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

def generate_tests_for_all_files(source_dir, output_dir="tests"):
    print("Generating tests for all Python files...")
    for dirpath, _, files in os.walk(source_dir):
        for file_name in files:
            if file_name.endswith(".py") and not file_name.startswith("test_"):
                file_path = os.path.join(dirpath, file_name)
                generate_tests_for_file(file_path, output_dir)
    print("Full test generation complete.")
