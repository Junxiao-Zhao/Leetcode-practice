# https://leetcode.com/problems/k-closest-points-to-origin/


def kClosest(points: list, k: int):
    from queue import PriorityQueue

    que = PriorityQueue()
    [que.put((-x**2 - y**2, i)) for i, (x, y) in enumerate(points[:k])]

    for i in range(k, len(points)):
        sum_sqrt, j = que.get()
        if -sum_sqrt > points[i][0]**2 + points[i][1]**2:
            que.put((-points[i][0]**2 - points[i][1]**2, i))
        else:
            que.put((sum_sqrt, j))

    ans = [points[que.get()[1]] for _ in range(k)]
    return ans
