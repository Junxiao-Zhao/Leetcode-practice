# https://leetcode.com/problems/score-of-parentheses/


def scoreOfParentheses(s: str):
    stack = []

    for each in s:
        if each == "(":
            stack.append(each)
        else:
            nums = 0
            left = stack.pop()
            if left == "(":
                stack.append(1)
                continue
            while left != "(":
                nums += left
                left = stack.pop()
            stack.append(2 * nums)

    return sum(stack)
