# https://leetcode.com/problems/all-paths-from-source-to-target/


def allPathsSourceTarget(graph: list):
    if len(graph) == 0:
        return []

    paths = list()
    end = len(graph) - 1

    def dfs(node: int, cur_path: list):
        cur_path.append(node)
        if node == end:
            paths.append(cur_path)
            return

        for each in graph[node]:
            dfs(each, cur_path.copy())

    dfs(0, [])

    return paths
