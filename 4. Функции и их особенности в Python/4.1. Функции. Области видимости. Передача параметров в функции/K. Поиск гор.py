def find_mountains(heights: list[int]) -> tuple[int, ...]:
    res = []
    for index, (left, middle, right) in enumerate(
        zip(heights, heights[1:], heights[2:]), 2
    ):
        if middle > left and middle > right:
            res.append(index)
    return tuple(res)
