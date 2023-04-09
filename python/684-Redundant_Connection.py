# https://leetcode.com/problems/redundant-connection/


def findRedundantConnection(edges: list):
    findCycle = False
    adj = dict()
    visited = dict()
    for start, end in edges:
        adj.setdefault(start, [])
        adj.setdefault(end, [])
        adj[start].append(end)
        adj[end].append(start)
        visited.setdefault(start, -1)
        visited.setdefault(end, -1)

    ans = None

    def dfs(node: int, cur_path: list, pre: int):
        nonlocal ans, findCycle
        if visited[node] == 0:
            cur_path.append(node)
            ans = cur_path
            findCycle = True
            return
        if findCycle or len(adj[node]) == 0:
            return

        cur_path.append(node)
        visited[node] = 0
        for each in adj[node]:
            if each != pre:
                dfs(each, cur_path.copy(), node)
        visited[node] = 1

    dfs(1, [], None)
    while ans[0] != ans[-1]:
        del ans[0]
    remove = [
        ([ans[i], ans[i + 1]] if ans[i] < ans[i + 1] else [ans[i + 1], ans[i]])
        for i in range(len(ans) - 1)
    ]
    for each in reversed(edges):
        if each in remove:
            return each


if __name__ == '__main__':
    edges = [[2, 7], [7, 8], [3, 6], [2, 5], [6, 8], [4, 8], [2, 8], [1, 8],
             [7, 10], [3, 9]]
    print(findRedundantConnection(edges))
