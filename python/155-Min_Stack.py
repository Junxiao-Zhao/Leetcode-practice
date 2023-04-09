# https://leetcode.com/problems/min-stack/


class MinStack:

    def __init__(self):
        self.stack = list()
        self.minstack = [float("inf")]

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minstack.append(min(val, self.minstack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
