# https://leetcode.com/problems/find-eventual-safe-states/


def eventualSafeNodes(graph: list):
    safe = [None] * len(graph)
    visited = [-1] * len(graph)

    def dfs(node: int):
        if visited[node] == 0:
            safe[node] = False
            return False

        if safe[node] is not None:
            return safe[node]

        if len(graph[node]) == 0:
            safe[node] = True
            visited[node] = 1
            return True

        visited[node] = 0
        isSafe = True
        for each in graph[node]:
            isSafe = isSafe and dfs(each)
            if not isSafe:
                break
        safe[node] = isSafe
        visited[node] = 1
        return safe[each]

    ans = []
    for i in range(len(graph)):
        if visited[i] == -1:
            dfs(i)
        if safe[i]:
            ans.append(i)

    return ans
