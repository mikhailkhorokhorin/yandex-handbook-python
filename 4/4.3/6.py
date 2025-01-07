# Сортировка слиянием
def merge(left: list, right: list) -> list:
    result = []
    while left and right:
        result.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
    return result + left + right


def merge_sort(array: list) -> list:
    if len(array) <= 1:
        return array
    return merge(merge_sort(array[:len(array) // 2]), merge_sort(array[len(array) // 2:]))
