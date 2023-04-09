# https://leetcode.com/problems/sum-of-distances-in-tree/


def sumOfDistancesInTree(n: int, edges: list):
    adj = [[] for _ in range(n)]

    for i, j in edges:
        adj[i].append(j)
        adj[j].append(i)

    dp = [0] * n
    size = [0] * n
    ans = [0] * n

    def dfs(node: int, parent: int):
        size[node] = 1
        dp[node] = 0

        for each in adj[node]:
            if each == parent:
                continue
            dfs(each, node)
            dp[node] += dp[each] + size[each]
            size[node] += size[each]

    def dfs2(node: int, parent: int):
        ans[node] = dp[node]

        for each in adj[node]:
            if each == parent:
                continue
            pu = dp[node]
            pv = dp[each]
            su = size[node]
            sv = size[each]

            dp[node] -= dp[each] + size[each]
            size[node] -= size[each]
            dp[each] += dp[node] + size[node]
            size[each] += size[node]

            dfs2(each, node)

            dp[node] = pu
            dp[each] = pv
            size[node] = su
            size[each] = sv

    dfs(0, -1)
    dfs2(0, -1)
    return ans


if __name__ == "__main__":
    edges = [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]
    print(sumOfDistancesInTree(6, edges))
