# https://leetcode.com/problems/flatten-nested-list-iterator/


class NestedIterator:

    def __init__(self, nestedList):
        self.stack = []
        while len(nestedList):
            self.stack.append(nestedList.pop())

    def next(self) -> int:
        return self.stack.pop().getInteger()

    def hasNext(self) -> bool:
        while len(self.stack):
            top = self.stack[-1]
            if top.isInteger():
                return True
            self.stack = self.stack[:-1] + top.getList()[::-1]
        return False
