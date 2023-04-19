# https://leetcode.com/problems/top-k-frequent-elements/

from collections import Counter
from queue import PriorityQueue


def topKFrequent(nums: list[int], k: int) -> list[int]:

    counts = Counter(nums)
    que = PriorityQueue()

    for n, c in counts.items():
        if que.qsize() < k or que.queue[0][0] < c:
            que.put([c, n])
        if que.qsize() > k:
            que.get()

    return [n for _, n in que.queue]


if __name__ == "__main__":
    nums = [3, 0, 1, 0]
    k = 1
    print(topKFrequent(nums, k))
