{
    i
    for i in numbers
    if i
    in [
        x
        for x in range(2, max(numbers) + 1)
        if all(x % y != 0 for y in range(2, int(x**0.5) + 1))
    ]
}
