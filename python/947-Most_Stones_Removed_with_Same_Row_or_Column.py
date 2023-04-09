# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/


class UnionFind:

    def __init__(self):
        self.parents = dict()
        self.count = 0

    def find(self, k: int):
        if self.parents.get(k, None) is None:
            self.count += 1
            self.parents[k] = k
        if self.parents[k] != k:
            self.parents[k] = self.find(self.parents[k])

        return self.parents[k]

    def union(self, k1: int, k2: int):
        par1 = self.find(k1)
        par2 = self.find(k2)
        if par1 != par2:
            self.parents[par1] = par2
            self.count -= 1


def removeStones(stones: list):
    uf = UnionFind()
    for stone in stones:
        uf.union(stone[0] + 10001, stone[1])

    return len(stones) - uf.count


if __name__ == "__main__":
    stones = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]
    print(removeStones(stones))
