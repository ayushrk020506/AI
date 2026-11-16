print("Ayush R Kallingal\n1WN24CS057")
def is_variable(x):
    return x[0].islower() and "(" not in x

def parse(expr):
    expr = expr.strip()
    if "(" not in expr:
        return expr
    name, args = expr.split("(", 1)
    args = args[:-1]
    result = []
    depth = 0
    start = 0
    for i, ch in enumerate(args):
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        elif ch == "," and depth == 0:
            result.append(args[start:i].strip())
            start = i + 1
    result.append(args[start:].strip())
    return name.strip(), result

def apply_substitution(expr, theta):
    if expr in theta:
        return apply_substitution(theta[expr], theta)
    if "(" not in expr:
        return expr
    name, args = parse(expr)
    return name + "(" + ",".join(
        apply_substitution(arg, theta) for arg in args
    ) + ")"

def occurs(var, expr, theta):
    expr = apply_substitution(expr, theta)
    if var == expr:
        return True
    if "(" not in expr:
        return False
    name, args = parse(expr)
    return any(occurs(var, arg, theta) for arg in args)

def unify_var(var, expr, theta):
    if var in theta:
        return unify(theta[var], expr, theta)

    if is_variable(expr) and expr in theta:
        return unify(var, theta[expr], theta)

    if occurs(var, expr, theta):
        return None

    theta[var] = expr
    return theta

def unify(e1, e2, theta=None):
    if theta is None:
        theta = {}

    e1 = apply_substitution(e1, theta)
    e2 = apply_substitution(e2, theta)

    if e1 == e2:
        return theta

    if is_variable(e1):
        return unify_var(e1, e2, theta)

    if is_variable(e2):
        return unify_var(e2, e1, theta)

    if "(" not in e1 or "(" not in e2:
        return None

    name1, args1 = parse(e1)
    name2, args2 = parse(e2)

    if name1 != name2 or len(args1) != len(args2):
        return None

    for a, b in zip(args1, args2):
        theta = unify(a, b, theta)
        if theta is None:
            return None

    return theta

e1 = input("Enter first expression: ")
e2 = input("Enter second expression: ")

result = unify(e1, e2)

if result is None:
    print("Unification Failed")
else:
    print("Unification Successful")
    print("Most General Unifier (MGU):")
    for var, value in result.items():
        print(var, "=", apply_substitution(value, result))
    print("Unified Expression:", apply_substitution(e1, result))