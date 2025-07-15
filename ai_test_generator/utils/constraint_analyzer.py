import ast

def get_param_constraints(func_node):
    constraints = {}

    for node in ast.walk(func_node):
        if isinstance(node, ast.If) and isinstance(node.test, ast.Compare):
            left = node.test.left
            comparator = node.test.comparators[0]
            if isinstance(left, ast.Name) and isinstance(comparator, (ast.Constant, ast.Num)):
                param = left.id
                value = comparator.value if isinstance(comparator, ast.Constant) else comparator.n
                op = type(node.test.ops[0]).__name__

                if param not in constraints:
                    constraints[param] = []

                constraints[param].append((op, value))

    return constraints
