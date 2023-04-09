# https://leetcode.com/problems/minesweeper/


def updateBoard(board: list, click: list):
    trick1 = [-1, 0, 1, 0, -1]
    trick2 = [-1, -1, 1, 1, -1]

    if board[click[0]][click[1]] == "M":
        board[click[0]][click[1]] = "X"
        return board

    def check_around(x, y):
        count = 0
        for k in range(4):
            i1, j1 = x + trick1[k], y + trick1[k + 1]
            i2, j2 = x + trick2[k], y + trick2[k + 1]
            if i1 >= 0 and i1 < len(board) and j1 >= 0 and j1 < len(
                    board[0]) and board[i1][j1] == "M":
                count += 1
            if i2 >= 0 and i2 < len(board) and j2 >= 0 and j2 < len(
                    board[0]) and board[i2][j2] == "M":
                count += 1
        return count

    pos = [click]

    while len(pos) > 0:
        x, y = pos.pop(0)

        if board[x][y] == "E":
            num = check_around(x, y)
            if num > 0:
                board[x][y] = str(num)
            else:
                for k in range(4):
                    i1, j1 = x + trick1[k], y + trick1[k + 1]
                    i2, j2 = x + trick2[k], y + trick2[k + 1]
                    if i1 >= 0 and i1 < len(board) and j1 >= 0 and j1 < len(
                            board[0]):
                        pos.append([i1, j1])
                    if i2 >= 0 and i2 < len(board) and j2 >= 0 and j2 < len(
                            board[0]):
                        pos.append([i2, j2])
                board[x][y] = "B"

    return board
