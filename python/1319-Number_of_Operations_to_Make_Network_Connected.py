# https://leetcode.com/problems/number-of-operations-to-make-network-connected/


class UnionFind:

    def __init__(self, n: int) -> None:
        self.parents = list(range(n))
        self.count = 0

    def find(self, k: int):
        if self.parents[k] != k:
            self.parents[k] = self.find(self.parents[k])
        return self.parents[k]

    def union(self, k1: int, k2: int):
        p1 = self.find(k1)
        p2 = self.find(k2)
        if p1 != p2:
            self.parents[p1] = p2
            self.count += 1


def makeConnected(n: int, connections: list):
    num_connect = len(connections)
    if n - 1 > num_connect:
        return -1

    uf = UnionFind(n)
    for c1, c2 in connections:
        uf.union(c1, c2)

    return n - uf.count - 1
