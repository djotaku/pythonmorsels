def add(matrix1, matrix2):
    return [[val1 + val2 for val1, val2 in zip(list1, list2)] for list1, list2 in zip(matrix1, matrix2)]


if __name__ == "__main__":
    matrix1 = [[1, -2], [-3, 4]]
    matrix2 = [[2, -1], [0, -1]]
    add(matrix1, matrix2)