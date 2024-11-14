from itertools import product


def postfix_expression(expression, variables, operator_list, priority_list):
    stack, result, lst = [], [], expression.split()
    for i in lst:
        if i in variables:
            result.append(i)
        elif i == "(":
            stack.append(i)
        elif i == ")":
            while stack[-1] != "(":
                result.append(operator_list[stack.pop()])
            stack.pop()
        elif i in operator_list.keys():
            while len(stack) and priority_list[i] >= priority_list[stack[-1]]:
                result.append(operator_list[stack.pop()])
            stack.append(i)
    for _ in range(len(stack)):
        result.append(operator_list[stack.pop()])
    return result


def result_of_expression(postfix_exp, variables):
    stack = []
    for i in range(len(postfix_exp)):
        if postfix_exp[i] in variables.keys():
            stack.append(variables[postfix_exp[i]])
        else:
            if postfix_exp[i] == "not":
                stack.append(not stack.pop())
            else:
                var2, var1 = stack.pop(), stack.pop()
                stack.append(eval(f"{var1} {postfix_exp[i]} {var2}"))
    return int(stack.pop())


def main():
    # Таблица истинности 3

    operator_list = {
        "not": "not",
        "and": "and",
        "or": "or",
        "^": "!=",
        "->": "<=",
        "~": "==",
    }

    priority_list = {
        "not": 0,
        "and": 1,
        "or": 2,
        "^": 3,
        "->": 4,
        "~": 5,
        "(": 6,
    }

    statement = input()
    var_all = sorted(set([i for i in statement if i.isupper()]))
    print(" ".join(var_all), "F")
    table = product([0, 1], repeat=len(var_all))
    statement = statement.replace("(", "( ").replace(")", " )")
    exp = postfix_expression(statement, var_all, operator_list, priority_list)

    for row in table:
        res = {}
        for k, v in zip(var_all, row):
            res[k] = v
        print(" ".join(str(x) for x in row), result_of_expression(exp, res))


if __name__ == "__main__":
    main()
