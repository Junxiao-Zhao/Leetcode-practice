# https://leetcode.ca/all/694.html


def numDistinctIslands(grid: list):
    trick = [-1, 0, 1, 0, -1]
    path = ""

    def dfs(i, j, dir):
        nonlocal path
        if not grid[i][j]:
            return

        grid[i][j] = 0
        path += dir
        for k in range(4):
            x, y = i + trick[k], j + trick[k + 1]
            if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]):
                dfs(x, y, str(k))
        path += "4"

    ans = []

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                dfs(i, j, "4")
                ans.append(path)
                path = ""

    return len(set(ans))


if __name__ == "__main__":
    grid = [[1, 1, 0, 1, 1], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [1, 1, 0, 1, 1]]
    print(numDistinctIslands(grid))
