def fragments(numbers: list[int]):
    result: list[list[int]] = [[numbers[0]]]
    for num in numbers[1:]:
        if num > result[-1][-1]:
            result[-1].append(num)
        else:
            result.append([num])
    return result
