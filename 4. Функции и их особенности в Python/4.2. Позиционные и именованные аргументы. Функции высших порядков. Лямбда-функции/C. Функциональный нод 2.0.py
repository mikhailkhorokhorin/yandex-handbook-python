def GCD(num1: int, num2: int) -> int:
    while num1 != 0 and num2 != 0:
        num1, num2 = (
            (num1 % num2, num2) if num1 > num2 else (num1, num2 % num1)
        )
    return num1 + num2


def gcd(*args) -> int:
    args, result = list(args), 0
    for i in range(len(args)):
        result = GCD(result, args[i])
    return result
