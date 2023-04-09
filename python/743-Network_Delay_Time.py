# https://leetcode.com/problems/network-delay-time/

from queue import PriorityQueue
import math


def networkDelayTime(times: list, n: int, k: int):
    adj = dict()
    for u, v, w in times:
        adj.setdefault(u, [])
        adj[u].append((w, v))

    min_time = [float("inf")] * (n + 1)
    min_time[0] = 0
    min_time[k] = 0

    que = PriorityQueue()
    que.put((0, k))

    while not que.empty():
        weight, node = que.get()

        if weight > min_time[node]:
            continue

        for next_w, next_node in adj.setdefault(node, []):
            if min_time[next_node] > min_time[node] + next_w:
                min_time[next_node] = min_time[node] + next_w
                que.put((min_time[next_node], next_node))

    return -1 if math.isinf(max(min_time)) else max(min_time)
