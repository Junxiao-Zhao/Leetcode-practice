# https://leetcode.com/problems/regions-cut-by-slashes/


class UnionFind:

    def __init__(self, n):
        self.count = 4 * n * n
        self.parents = list(range(self.count))

    def find(self, k: int):
        if self.parents[k] != k:
            self.parents[k] = self.find(self.parents[k])

        return self.parents[k]

    def union(self, k1: int, k2: int):
        par1 = self.find(k1)
        par2 = self.find(k2)
        if par1 != par2:
            self.parents[par1] = par2
            self.count -= 1


def regionsBySlashes(grid: list):
    n = len(grid)
    uf = UnionFind(n)

    for i in range(n):
        for j in range(n):
            index = 4 * (i * n + j)
            if grid[i][j] == "/":
                uf.union(index, index + 3)
                uf.union(index + 1, index + 2)
            elif grid[i][j] == "\\":
                uf.union(index, index + 1)
                uf.union(index + 2, index + 3)
            else:
                uf.union(index, index + 1)
                uf.union(index + 1, index + 2)
                uf.union(index + 2, index + 3)

            if j + 1 < n:
                uf.union(index + 1, 4 * (i * n + j + 1) + 3)
            if i + 1 < n:
                uf.union(index + 2, 4 * ((i + 1) * n + j))

    return uf.count
