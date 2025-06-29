def is_palindrome(n) -> bool:
    return str(n) == str(n)[::-1] if isinstance(n, int) else n == n[::-1]
