# https://leetcode.com/problems/rotting-oranges/


def orangesRotting(grid: list):
    num_freash = 0
    rotten = []

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                num_freash += 1
            elif grid[i][j] == 2:
                rotten.append([i, j])

    rotten_next = []

    trick = [-1, 0, 1, 0, -1]
    count = 0
    while len(rotten) > 0:
        i, j = rotten.pop(0)

        for k in range(4):
            x = i + trick[k]
            y = j + trick[k + 1]
            if x >= 0 and x < len(grid) and y >= 0 and y < len(
                    grid[0]) and grid[x][y] == 1:
                grid[x][y] = 2
                rotten_next.append([x, y])
                num_freash -= 1

        if len(rotten) == 0:
            if len(rotten_next) > 0:
                count += 1
            rotten, rotten_next = rotten_next, rotten

    return count if num_freash == 0 else -1
