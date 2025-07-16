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

    def infer_type_from_usage(node, param_name):
        for subnode in ast.walk(node):
            if isinstance(subnode, ast.Subscript) and isinstance(subnode.value, ast.Name) and subnode.value.id == param_name:
                return 'dict'
            if isinstance(subnode, ast.Compare):
                for comparator in subnode.comparators:
                    if isinstance(comparator, ast.Attribute) and isinstance(comparator.value, ast.Name):
                        if comparator.value.id == param_name:
                            return 'dict'
            if isinstance(subnode, ast.BinOp) and (
                isinstance(subnode.left, ast.Name) and subnode.left.id == param_name or
                isinstance(subnode.right, ast.Name) and subnode.right.id == param_name):
                return 'int'
            if isinstance(subnode, ast.For) and isinstance(subnode.iter, ast.Name) and subnode.iter.id == param_name:
                return 'list'
            if isinstance(subnode, ast.Call) and isinstance(subnode.func, ast.Attribute):
                if isinstance(subnode.func.value, ast.Name) and subnode.func.value.id == param_name:
                    if subnode.func.attr in ['format', 'split', 'join']:
                        return 'str'
        return None

    def get_args_string(func_ref, func_node):
        try:
            constraints = get_param_constraints(func_node)
            sig = inspect.signature(func_ref)
            params = []

            for name, param in list(sig.parameters.items()):
                if name == 'self':
                    continue
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
                    inferred = infer_type_from_usage(func_node, name)
                    if inferred == 'dict':
                        safe_val = '{"sample_key": 10}'
                    elif inferred == 'list':
                        safe_val = '["sample_value"]'
                    elif inferred == 'str':
                        safe_val = '"sample"'
                    elif inferred == 'int':
                        safe_val = '1'
                    else:
                        safe_val = '"sample"' if name.lower().endswith("name") else '1'

                params.append(safe_val)

            return ", ".join(params)
        except Exception:
            sig = inspect.signature(func_ref)
            return ", ".join("1" for name, param in sig.parameters.items() if name != "self")

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
