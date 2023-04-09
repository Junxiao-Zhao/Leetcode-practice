# https://leetcode.ca/all/490.html


def hasPath(maze: list, start: list, end: list):
    pos = [start + [None]]
    UP = -1
    DOWN = 1
    LEFT = 2
    RIGHT = -2
    visited = [[0] * len(maze[0]) for _ in range(len(maze))]

    while len(pos) > 0:
        x, y, pre = pos.pop(0)
        if [x, y] == end:
            return True

        visited[x][y] = 1

        for k in [UP, DOWN, LEFT, RIGHT]:
            if k == pre:
                continue

            i, j = x, y
            if k == DOWN:
                while i < len(maze) - 1 and maze[i + 1][j] != 1:
                    i += 1
            elif k == UP:
                while i > 0 and maze[i - 1][j] != 1:
                    i -= 1
            elif k == LEFT:
                while j > 0 and maze[i][j - 1] != 1:
                    j -= 1
            else:
                while j < len(maze[0]) - 1 and maze[i][j + 1] != 1:
                    j += 1

            if not visited[i][j]:
                pos.append([i, j, -k])

    return False


if __name__ == "__main__":
    maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1],
            [0, 0, 0, 0, 0]]
    print(hasPath(maze, [0, 4], [3, 2]))
