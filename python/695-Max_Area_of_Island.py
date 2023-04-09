# https://leetcode.com/problems/max-area-of-island/


def maxAreaOfIsland(grid: list):
    visited = [[0] * len(grid[0]) for _ in range(len(grid))]
    trick = [-1, 0, 1, 0, -1]

    def dfs(i, j):
        if grid[i][j] == 0:
            return 0

        area = 1
        visited[i][j] = 1

        for k in range(4):
            x = i + trick[k]
            y = j + trick[k + 1]
            if x >= 0 and x < len(grid) and y >= 0 and y < len(
                    grid[0]) and visited[x][y] == 0:
                area += dfs(x, y)

        return area

    max_area = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if visited[i][j] == 0:
                max_area = max(max_area, dfs(i, j))

    return max_area


if __name__ == '__main__':
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    print(maxAreaOfIsland(grid))
