# https://leetcode.com/problems/01-matrix/


def updateMatrix(mat: list):
    dp = [[100000] * len(mat[0]) for _ in range(len(mat))]
    trick = [-1, 0, 1, 0, -1]
    store = []

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if not mat[i][j]:
                dp[i][j] = 0
                store.append([i, j])

    next = []
    val = 1
    while len(store) > 0:
        i, j = store.pop(0)

        for k in range(4):
            x = i + trick[k]
            y = j + trick[k + 1]
            if x >= 0 and x < len(mat) and y >= 0 and y < len(
                    mat[0]) and val < dp[x][y]:
                dp[x][y] = val
                next.append([x, y])

        if len(store) == 0:
            store, next = next, store
            val += 1

    return dp
