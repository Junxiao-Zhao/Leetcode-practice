# https://leetcode.com/problems/generate-parentheses/


def generateParenthesis(n: int):
    ans = []

    def backtrack(S, left, right):
        if len(S) == 2 * n:
            ans.append(''.join(S))
            return
        if left < n:
            S.append('(')
            backtrack(S, left + 1, right)
            S.pop()
        if right < left:
            S.append(')')
            backtrack(S, left, right + 1)
            S.pop()

    backtrack([], 0, 0)
    return ans


if __name__ == "__main__":
    print(generateParenthesis(4))
