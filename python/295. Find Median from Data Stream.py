# https://leetcode.com/problems/find-median-from-data-stream/description/

from queue import PriorityQueue


class MedianFinder:

    def __init__(self):
        self.que1 = PriorityQueue()
        self.que2 = PriorityQueue()

    def addNum(self, num: int) -> None:

        if self.que1.empty() or num < self.que1.queue[0][1]:
            self.que1.put([-num, num])
            if self.que1.qsize() > self.que2.qsize() + 1:
                _, num = self.que1.get()
                self.que2.put([num, num])
        else:
            self.que2.put([num, num])
            if self.que2.qsize() > self.que1.qsize():
                _, num = self.que2.get()
                self.que1.put([-num, num])

    def findMedian(self) -> float:

        if self.que1.qsize() > self.que2.qsize():
            return self.que1.queue[0][1]
        else:
            return (self.que1.queue[0][1] + self.que2.queue[0][1]) / 2
