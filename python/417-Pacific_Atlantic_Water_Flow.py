# https://leetcode.com/problems/pacific-atlantic-water-flow/


def pacificAtlantic(heights: list):
    m = len(heights)
    n = len(heights[0])

    to_pacif = [[0] * n for _ in range(m)]
    to_atlan = [[0] * n for _ in range(m)]

    trick = [-1, 0, 1, 0, -1]

    def flow(matrix, a, b):

        if matrix[a][b]:
            return
        matrix[a][b] = 1
        for k in range(4):
            x = a + trick[k]
            y = b + trick[k + 1]
            if x >= 0 and x < m and y >= 0 and y < n and heights[a][
                    b] <= heights[x][y]:
                flow(matrix, x, y)

    for i in range(0, m):
        flow(to_pacif, i, 0)
        flow(to_atlan, i, n - 1)
    for j in range(0, n):
        flow(to_pacif, 0, j)
        flow(to_atlan, m - 1, j)

    pos = []
    for i in range(m):
        for j in range(n):
            if to_pacif[i][j] == 1 and to_atlan[i][j] == 1:
                pos.append([i, j])

    return pos


if __name__ == "__main__":
    heights = [[2, 1], [1, 2]]
    print(pacificAtlantic(heights))
