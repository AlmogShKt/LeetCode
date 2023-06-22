#200. Number of Islands


def numIslands(grid) -> int:
    num_islands = 0

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = set()

    def set_isalnd_zeros(grid, row, col):
        if (0 <= row < len(grid)) and (0 <= col < len(grid[0])) and grid[row][col] == "1" and (row, col) not in visited:
            # grid[row][col] = "0"
            visited.add((row, col))
            for row_inc, col_inc in directions:
                set_isalnd_zeros(grid, row + row_inc, col + col_inc)

    m, n = len(grid), len(grid[0])

    for row in range(m):
        for col in range(n):
            if grid[row][col] == "1" and (row, col) not in visited:
                num_islands += 1
                set_isalnd_zeros(grid, row, col)

    return num_islands


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

print(numIslands(grid))
