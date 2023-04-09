# https://leetcode.com/problems/remove-invalid-parentheses/


def removeInvalidParentheses(s: str):
    lremove = rremove = 0

    for each in s:
        if each == '(':
            lremove += 1
        elif each == ')':
            if lremove > 0:
                lremove -= 1
            else:
                rremove += 1

    def is_valid(s: str):
        count = 0
        for each in s:
            if each == '(':
                count += 1
            elif each == ')':
                count -= 1
                if count < 0:
                    return False
        return count == 0

    ans = []

    def backtracking(s: str, start: int, lremove: int, rremove: int):
        if lremove == 0 and rremove == 0:
            if is_valid(s):
                ans.append(s)
            return

        for i in range(start, len(s)):
            if i > start and s[i] == s[i - 1]:
                continue
            if lremove + rremove > len(s) - i:
                break
            if lremove > 0 and s[i] == '(':
                backtracking(s[:i] + s[i + 1:], i, lremove - 1, rremove)
            elif rremove > 0 and s[i] == ')':
                backtracking(s[:i] + s[i + 1:], i, lremove, rremove - 1)

    backtracking(s, 0, lremove, rremove)
    return ans
