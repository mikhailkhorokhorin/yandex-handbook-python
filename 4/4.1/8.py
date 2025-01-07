# А роза упала на лапу Азора 7.0
def is_palindrome(n) -> bool:
    return str(n) == str(n)[::-1] if isinstance(n, int) else n == n[::-1]
