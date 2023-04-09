# https://leetcode.com/problems/number-of-provinces/


def findCircleNum(isConnected: list):
    visited = [0] * len(isConnected)
    adj = dict()

    for i in range(len(isConnected)):
        for j in range(len(isConnected[0])):
            if i != j and isConnected[i][j]:
                adj.setdefault(i, [])
                adj[i].append(j)

    def dfs(city: int):
        visited[city] = 1
        for each in adj.setdefault(city, []):
            if not visited[each]:
                dfs(each)

    count = 0
    for i in range(len(visited)):
        if not visited[i]:
            count += 1
            dfs(i)

    return count
