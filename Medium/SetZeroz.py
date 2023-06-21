def setZeroes(matrix):
    row_0 = [0] * len(matrix)
    col_0 = [0] * len(matrix[0])

    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == 0:
                row_0[r] = 1
                col_0[c] = 1

    for r, flag in enumerate(row_0):
        if flag:
            for cell in range(len(matrix[0])):
                matrix[r][cell] = 0

    for c, flag in enumerate(col_0):
        if flag:
            for cell in range(len(matrix)):
                matrix[cell][c] = 0

    print(matrix)


matrix = [[1,1,1],[1,0,1],[1,1,1]]
setZeroes(matrix)