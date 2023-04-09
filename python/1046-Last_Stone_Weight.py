# https://leetcode.com/problems/last-stone-weight/

from queue import PriorityQueue


def lastStoneWeight(stones: list):
    que = PriorityQueue()
    for each in stones:
        que.put(-each)

    while que.qsize() > 1:
        st1 = -que.get()
        st2 = -que.get()
        if st1 > st2:
            que.put(st2 - st1)

    return -que.get() if que.qsize() > 0 else 0
