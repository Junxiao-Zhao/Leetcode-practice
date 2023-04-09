# https://leetcode.com/problems/clone-graph/


class Node:

    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def cloneGraph(node: Node):
    if not node:
        return None

    visited = dict()

    def dfs(node: Node):
        if visited.setdefault(node, None):
            return visited[node]

        visited[node] = Node(node.val)
        for each in node.neighbors:
            visited[node].neighbors.append(dfs(each))

        return visited[node]

    return dfs(node)
