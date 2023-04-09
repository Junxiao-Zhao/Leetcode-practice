# https://leetcode.com/problems/number-of-closed-islands/


def closedIsland(grid: list):
    visited = [[0] * len(grid[0]) for _ in range(len(grid))]
    trick = [-1, 0, 1, 0, -1]

    def dfs(i: int, j: int, surrounded: bool):

        if grid[i][j] or visited[i][j]:
            return surrounded

        visited[i][j] = 1
        if i == 0 or i == len(grid) - 1 or j == 0 or j == len(grid[0]) - 1:
            surrounded = False
        for k in range(4):
            x = i + trick[k]
            y = j + trick[k + 1]
            if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]):
                surrounded = dfs(x, y, surrounded)
        return surrounded

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if not visited[i][j] and not grid[i][j] and dfs(i, j, True):
                count += 1

    return count


if __name__ == "__main__":
    grid = [[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0],
            [1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 0]]
    print(closedIsland(grid))
