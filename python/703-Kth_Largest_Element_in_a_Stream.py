# https://leetcode.com/problems/kth-largest-element-in-a-stream/

from queue import PriorityQueue


class KthLargest:

    def __init__(self, k: int, nums: list):
        self.k = k
        self.que = PriorityQueue()
        for each in nums:
            self.que.put(each)

    def add(self, val: int) -> int:
        self.que.put(val)
        while self.que.qsize() > self.k:
            self.que.get()

        temp = self.que.get()
        self.que.put(temp)
        return temp


if __name__ == '__main__':
    obj = KthLargest(1, [])
    array = [-3, -2, -4, 0, 4]
    for each in array:
        print(obj.add(each))
