# https://leetcode.com/problems/24-game/


def judgePoint24(cards: list):
    epsilon = 1e-6
    add, mult, minus = 0, 1, 2

    def backtracking(cur_cards: list):
        if len(cur_cards) == 1:
            return abs(cur_cards[0] - 24) < epsilon

        for i, a in enumerate(cur_cards):
            for j, b in enumerate(cur_cards):
                if i != j:
                    new_sol = []
                    for k, c in enumerate(cur_cards):
                        if k != i and k != j:
                            new_sol.append(c)
                    for k in range(4):
                        if k < 2 and i > j:
                            continue
                        if k == add:
                            new_sol.append(a + b)
                        elif k == mult:
                            new_sol.append(a * b)
                        elif k == minus:
                            new_sol.append(a - b)
                        else:
                            if abs(b) < epsilon:
                                continue
                            new_sol.append(a / b)
                        if backtracking(new_sol):
                            return True
                        new_sol.pop()
        return False

    return backtracking(cards)
