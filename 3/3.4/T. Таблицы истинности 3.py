from itertools import product


def postfix(
    expression: str, variables: list, operators: dict, priorities: dict
) -> list:
    stack, result = [], []
    for token in expression.split():
        if token in variables:
            result.append(token)
        elif token == "(":
            stack.append(token)
        elif token == ")":
            while stack[-1] != "(":
                result.append(operators[stack.pop()])
            stack.pop()
        elif token in operators:
            while stack and priorities[token] >= priorities[stack[-1]]:
                result.append(operators[stack.pop()])
            stack.append(token)
    while stack:
        result.append(operators[stack.pop()])
    return result


def result(postfix_exp: list, variables: dict) -> int:
    stack = []
    for token in postfix_exp:
        if token in variables:
            stack.append(variables[token])
        else:
            if token == "not":
                stack.append(not stack.pop())
            else:
                var2, var1 = stack.pop(), stack.pop()
                stack.append(eval(f"{var1} {token} {var2}"))
    return int(stack.pop())


def main() -> None:
    operators = {
        "not": "not",
        "and": "and",
        "or": "or",
        "^": "!=",
        "->": "<=",
        "~": "==",
    }
    priorities = {
        key: value
        for value, key in enumerate(["not", "and", "or", "^", "->", "~", "("])
    }

    statement = input()
    variables = sorted(set(filter(str.isupper, statement)))
    print(" ".join(variables), "F")

    statement = statement.replace("(", "( ").replace(")", " )")
    exp = postfix(statement, variables, operators, priorities)

    for row in product([0, 1], repeat=len(variables)):
        res = dict(zip(variables, row))
        print(" ".join(map(str, row)), result(exp, res))


if __name__ == "__main__":
    main()
