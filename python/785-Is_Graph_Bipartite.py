# https://leetcode.com/problems/is-graph-bipartite/


def isBipartite(graph: list):
    visited = dict()

    for i in range(len(graph)):
        depth = 0
        if visited.setdefault(i, depth) == 0:
            cur_layer = [i]
            next_layer = []

            while len(cur_layer) > 0:
                node = cur_layer.pop(0)

                for each in graph[node]:
                    if visited.setdefault(each, -1) == depth:
                        return False
                    elif visited[each] != -1:
                        continue
                    visited[each] = depth + 1
                    next_layer.append(each)

                if len(cur_layer) == 0:
                    cur_layer, next_layer = next_layer, cur_layer
                    depth += 1

    return True


if __name__ == "__main__":
    graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
    print(isBipartite(graph))
