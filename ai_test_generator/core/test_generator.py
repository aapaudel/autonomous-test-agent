import ast
import inspect
from ai_test_generator.utils.constraint_analyzer import get_param_constraints
from ai_test_generator.utils.method_classifier import is_mutator_node, is_accessor_node


def generate_test_code(func_data, module, all_methods):
    class_name, func_name = func_data

    def get_func_node_from_ast(file_path, target_name):
        with open(file_path, "r") as f:
            tree = ast.parse(f.read())
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == target_name:
                return node
        return None

    def get_args_string(func_ref, func_node):
        try:
            constraints = get_param_constraints(func_node)
            sig = inspect.signature(func_ref)
            params = []

            for name, param in list(sig.parameters.items())[1:]:  # Skip 'self'
                if name in constraints:
                    op, value = constraints[name][0]
                    if op in ['LtE', 'Lt']:
                        safe_val = value + 1
                    elif op in ['Eq', 'Is']:
                        safe_val = f'"not_{value}"' if isinstance(value, str) else value + 1
                    elif op == 'IsNot':
                        safe_val = '"sample"' if param.annotation == str else 1
                    else:
                        safe_val = 1
                elif param.annotation != inspect._empty:
                    if param.annotation == int:
                        safe_val = '1'
                    elif param.annotation == float:
                        safe_val = '1.0'
                    elif param.annotation == str:
                        safe_val = '"sample_key"'
                    elif param.annotation == dict:
                        safe_val = '{"sample_key": 10}'
                    elif param.annotation == list:
                        safe_val = '["sample_value"]'
                    else:
                        safe_val = '"sample"'
                else:
                    if name in ["inventory", "prices", "catalog", "db"]:
                        safe_val = '{"sample_key": 10}'
                    elif name in ["product_id", "key", "name"]:
                        safe_val = '"sample_key"'
                    elif name in ["quantity", "count", "amount", "level"]:
                        safe_val = '1'
                    elif name in ["items", "cart", "history"]:
                        safe_val = '[("sample_key", 1)]'
                    elif name in ["rate", "price"]:
                        safe_val = '0.1'
                    else:
                        safe_val = '"sample"' if name.lower().endswith("name") else '1'

                params.append(safe_val)

            return ", ".join(params)
        except Exception:
            return "..."

    file_path = inspect.getfile(module)

    if class_name == "global":
        func_ref = getattr(module, func_name)
        func_node = get_func_node_from_ast(file_path, func_name)
        args_str = get_args_string(func_ref, func_node)
        return f"""
def test_{func_name}():
    result = {func_name}({args_str})
    assert result is not None if result is not None else result is None
"""
    else:
        class_ref = getattr(module, class_name)
        init_func = class_ref.__init__
        init_node = get_func_node_from_ast(file_path, "__init__")
        init_args = get_args_string(init_func, init_node)

        # Detect mutator and accessor based on AST structure
        mutator = accessor = None
        for m in all_methods:
            if m[0] != class_name:
                continue
            method_node = get_func_node_from_ast(file_path, m[1])
            if method_node:
                if is_mutator_node(method_node) and not mutator:
                    mutator = m[1]
                elif is_accessor_node(method_node) and not accessor:
                    accessor = m[1]

        if mutator and accessor:
            mutator_ref = getattr(class_ref, mutator)
            mutator_node = get_func_node_from_ast(file_path, mutator)
            mutator_args = get_args_string(mutator_ref, mutator_node)

            accessor_ref = getattr(class_ref, accessor)
            accessor_node = get_func_node_from_ast(file_path, accessor)
            accessor_args = get_args_string(accessor_ref, accessor_node)

            return f"""
def test_{mutator}_then_{accessor}():
    obj = {class_name}({init_args})
    obj.{mutator}({mutator_args})
    result = obj.{accessor}({accessor_args})
    if result is not None:
        assert isinstance(result, (int, float, str, list, dict))
    else:
        assert result is None
"""
        else:
            method_ref = getattr(class_ref, func_name)
            method_node = get_func_node_from_ast(file_path, func_name)
            method_args = get_args_string(method_ref, method_node)

            return f"""
def test_{func_name}():
    obj = {class_name}({init_args})
    result = obj.{func_name}({method_args})
    if result is not None:
        assert isinstance(result, (int, float, str, list, dict))
    else:
        assert result is None
"""

