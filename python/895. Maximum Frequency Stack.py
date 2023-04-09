from queue import PriorityQueue
from collections import defaultdict


class FreqStack:

    def __init__(self):
        self.count = defaultdict(int)
        self.fstack = PriorityQueue()
        self.count_same = defaultdict(int)

    def push(self, val: int) -> None:
        num = self.count[val] + 1
        self.count[val] = num
        self.count_same[num] += 1
        self.fstack.put(
            [-self.count[val] - 0.0001 * self.count_same[num], val])

    def pop(self) -> int:
        nc, val = self.fstack.get()
        self.count[val] -= 1
        return val


freqStack = FreqStack()
freqStack.push(5)
# The stack is [5]
freqStack.push(7)
# The stack is [5,7]
freqStack.push(5)
# The stack is [5,7,5]
freqStack.push(7)
# The stack is [5,7,5,7]
freqStack.push(4)
# The stack is [5,7,5,7,4]
freqStack.push(5)
# The stack is [5,7,5,7,4,5]
freqStack.pop()
# return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
freqStack.pop()
# return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
freqStack.pop()
# return 5, as 5 is the most frequent. The stack becomes [5,7,4].
freqStack.pop()
