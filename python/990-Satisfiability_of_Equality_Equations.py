# https://leetcode.com/problems/satisfiability-of-equality-equations/


class UnionFind:

    def __init__(self) -> None:
        self.parents = dict()

    def find(self, e: str):
        if self.parents.setdefault(e, e) != e:
            self.parents[e] = self.find(self.parents[e])
        return self.parents[e]

    def union(self, e1: str, e2: str):
        p1 = self.find(e1)
        p2 = self.find(e2)

        if p1 != p2:
            self.parents[p1] = p2


def equationsPossible(equations: list):
    uf_equ = UnionFind()

    for each in equations:
        if each[1] == "=":
            uf_equ.union(each[0], each[3])

    for each in equations:
        if each[1] == "!" and uf_equ.find(each[0]) == uf_equ.find(each[3]):
            return False

    return True


if __name__ == "__main__":
    equations = [
        "q!=s", "n==p", "s==m", "y!=h", "p==s", "l==t", "q==p", "b!=r", "j==w",
        "y!=u", "a!=f", "s==v", "n!=a", "s!=o"
    ]
    # print(sorted(equations, key=lambda x: x[1], reverse=True))
    print(equationsPossible(equations))
