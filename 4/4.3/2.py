def recursive_digit_sum(num: int) -> int:
    return num % 10 + recursive_digit_sum(num // 10) if num != 0 else 0
