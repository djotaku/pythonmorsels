def add(matrix1, matrix2):
    summed = [
        val1 + val2
        for list1, list2 in zip(matrix1, matrix2)
        for val1, val2 in zip(list1, list2)
    ]
    print(summed)
    for list1, list2 in zip(matrix1, matrix2):

        for val1, val2 in zip(list1, list2):
            print(val1+val2)

    return list(zip(matrix1, matrix2))


if __name__ == "__main__":
    matrix1 = [[1, -2], [-3, 4]]
    matrix2 = [[2, -1], [0, -1]]
    add(matrix1, matrix2)