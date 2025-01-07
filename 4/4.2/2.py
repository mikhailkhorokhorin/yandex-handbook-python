# Генератор матриц
def make_matrix(size, value: int = 0) -> list:
    if isinstance(size, int):
        return [[value for i in range(size)] for j in range(size)]
    return [[value for i in range(size[0])] for j in range(size[1])]
