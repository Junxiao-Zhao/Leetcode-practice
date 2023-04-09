# https://leetcode.com/problems/basic-calculator-ii/


def calculate(s: str):
    n = len(s)
    stack = []
    preSign = '+'
    num = 0
    for i in range(n):
        if s[i] != ' ' and s[i].isdigit():
            num = num * 10 + ord(s[i]) - ord('0')
        if i == n - 1 or s[i] in '+-*/':
            if preSign == '+':
                stack.append(num)
            elif preSign == '-':
                stack.append(-num)
            elif preSign == '*':
                stack.append(stack.pop() * num)
            else:
                stack.append(int(stack.pop() / num))
            preSign = s[i]
            num = 0
    return sum(stack)
