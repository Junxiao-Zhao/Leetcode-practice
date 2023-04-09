# https://leetcode.ca/all/286.html

INF = 2147483647


def wallsAndGates(rooms: list):
    trick = [-1, 0, 1, 0, -1]

    def bfs(loc: list):
        pos = [loc]

        while len(pos) > 0:
            i, j = pos.pop(0)

            for k in range(4):
                x, y = i + trick[k], j + trick[k + 1]
                if x >= 0 and x < len(rooms) and y >= 0 and y < len(
                        rooms[0]) and rooms[x][y] > rooms[i][j]:
                    rooms[x][y] = rooms[i][j] + 1
                    pos.append([x, y])

    for i in range(len(rooms)):
        for j in range(len(rooms[0])):
            if rooms[i][j] == 0:
                bfs([i, j])

    return rooms


if __name__ == "__main__":
    rooms = [[INF, -1, 0, INF], [INF, INF, INF, -1], [INF, -1, INF, -1],
             [0, -1, INF, INF]]
    print(wallsAndGates(rooms))
