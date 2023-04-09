# https://leetcode.com/problems/number-of-islands/


def numIslands(grid: list):
    visited = [[0] * len(grid[0]) for _ in range(len(grid))]
    trick = [-1, 0, 1, 0, -1]
    count = 0

    def dfs(i: int, j: int):
        if visited[i][j] or not int(grid[i][j]):
            return

        visited[i][j] = 1
        for k in range(4):
            x = i + trick[k]
            y = j + trick[k + 1]
            if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]):
                dfs(x, y)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if not visited[i][j] and int(grid[i][j]):
                count += 1
                dfs(i, j)

    return count


if __name__ == "__main__":
    grid = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]
    print(numIslands(grid))
