# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/
from queue import PriorityQueue


def shortestPath(grid: list, k: int):
    start = [0, 0]
    end = [len(grid) - 1, len(grid[0]) - 1]
    trick = [-1, 0, 1, 0, -1]

    if k >= end[0] + end[1] - 1:
        return end[0] + end[1]

    pos = PriorityQueue()
    pos.put([-k, start])
    next_pos = PriorityQueue()
    path_len = 0

    visited = [[None] * len(grid[0]) for _ in range(len(grid))]
    visited[0][0] = k

    while not pos.empty():
        _, [i, j] = pos.get()
        n = visited[i][j]

        if [i, j] == end:
            return path_len

        for a in range(4):
            x, y = i + trick[a], j + trick[a + 1]
            if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]):
                if grid[x][y] == 0 and (visited[x][y] is None
                                        or visited[x][y] < n):
                    next_pos.put([-n, [x, y]])
                    visited[x][y] = n
                elif grid[x][y] == 1 and n > 0 and (visited[x][y] is None
                                                    or visited[x][y] < n - 1):
                    next_pos.put([-n + 1, [x, y]])
                    visited[x][y] = n - 1

        if pos.empty():
            pos, next_pos = next_pos, pos
            path_len += 1

    return -1


if __name__ == "__main__":
    grid = [[0, 1, 0, 0, 0, 1, 0, 0], [0, 1, 0, 1, 0, 1, 0, 1],
            [0, 0, 0, 1, 0, 0, 1, 0]]
    print(shortestPath(grid, 1))
