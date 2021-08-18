def _traverse(matrix):
    result = []
    size = len(matrix)

    for loop in range(size // 2 + size % 2):

        for i in range(0 + loop, size - loop):
            elem = matrix[i][0 + loop]
            result.append(elem)

        for j in range((0 + loop) + 1, size - loop):
            elem = matrix[(size - 1) - loop][j]
            result.append(elem)

        for i in range((size - 1) - loop - 1, 0 + loop - 1, -1):
            elem = matrix[i][(size - 1) - loop]
            result.append(elem)

        for j in range((size - 1) - loop - 1, 0 + loop, -1):
            elem = matrix[(0 + loop)][j]
            result.append(elem)

    return result
