# https://leetcode.com/problems/game-of-life/


def gameOfLife(board: list):
    trick1 = [-1, 0, 1, 0, -1]
    trick2 = [-1, -1, 1, 1, -1]
    change = []

    def checkStatus(i, j):
        live = 0
        for k in range(4):
            x1, y1 = i + trick1[k], j + trick1[k + 1]
            x2, y2 = i + trick2[k], j + trick2[k + 1]
            if x1 >= 0 and x1 < len(board) and y1 >= 0 and y1 < len(board[0]):
                if board[x1][y1]:
                    live += 1
            if x2 >= 0 and x2 < len(board) and y2 >= 0 and y2 < len(board[0]):
                if board[x2][y2]:
                    live += 1

        if board[i][j] and (live < 2 or live > 3):
            change.append([i, j])
        if not board[i][j] and live == 3:
            change.append([i, j])

    for i in range(len(board)):
        for j in range(len(board[0])):
            checkStatus(i, j)

    for i, j in change:
        board[i][j] = 1 ^ board[i][j]
