def spiralOrder(matrix):
    # The borders of the matrix right, down , left , up
    border = {
        "right": len(matrix[0]),
        "down": len(matrix),
        "left": 0,
        "up": 0
    }
    output = []
    output_size = len(matrix) * len(matrix[0])
    # When we added all the numbers in the matrix wwe can stop the run
    while len(output) < output_size:
        # right
        for c in range(border["left"], border["right"]):
            output.append(matrix[border["up"]][c])
        border["up"] += 1

        if len(output) == output_size:
            break

        # down
        for r in range(border["up"], border["down"]):
            output.append(matrix[r][border["right"] - 1])
        border["right"] -= 1
        if len(output) == output_size:
            break

        # left
        for c in range(border["right"] - 1, border["left"] - 1, -1):
            output.append(matrix[border["down"] - 1][c])
        border["down"] -= 1
        if len(output) == output_size:
            break

        # up
        for r in range(border["down"] - 1, border["up"] + 1):
            output.append(matrix[r][border["left"]])

        border["left"] += 1
    return output

    print(output)


matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
spiralOrder(matrix)
