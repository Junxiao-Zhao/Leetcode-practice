# https://leetcode.com/problems/implement-stack-using-queues/


class MyStack:

    def __init__(self):
        self.que1 = []
        self.que2 = []

    def push(self, x: int) -> None:
        if len(self.que2):
            self.que2.append(x)
        else:
            self.que1.append(x)

    def pop(self) -> int:
        if len(self.que1):
            while len(self.que1) > 1:
                self.que2.append(self.que1.pop(0))
            return self.que1.pop(0)
        else:
            while len(self.que2) > 1:
                self.que1.append(self.que2.pop(0))
            return self.que2.pop(0)

    def top(self) -> int:
        if len(self.que1):
            while len(self.que1) > 1:
                self.que2.append(self.que1.pop(0))
            a = self.que1.pop(0)
            self.que2.append(a)
            return a
        else:
            while len(self.que2) > 1:
                self.que1.append(self.que2.pop(0))
            a = self.que2.pop(0)
            self.que1.append(a)
            return a

    def empty(self) -> bool:
        return len(self.que1) == 0 and len(self.que2) == 0
