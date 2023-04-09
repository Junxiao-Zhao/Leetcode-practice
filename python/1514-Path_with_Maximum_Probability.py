# https://leetcode.com/problems/path-with-maximum-probability/

from queue import PriorityQueue


def maxProbability(n: int, edges: list, succProb: list, start: int, end: int):
    adj = dict()

    for i, [s, t] in enumerate(edges):
        adj.setdefault(s, [])
        adj[s].append((succProb[i], t))
        adj.setdefault(t, [])
        adj[t].append((succProb[i], s))

    que = PriorityQueue()
    que.put((-1, start))
    prob_start = [0] * n
    prob_start[start] = 1

    while not que.empty():
        prob, cur = que.get()
        prob = -prob

        if prob < prob_start[cur]:
            continue
        for pro_next, node_next in adj.setdefault(cur, []):
            if prob_start[node_next] < prob_start[cur] * pro_next:
                prob_start[node_next] = prob_start[cur] * pro_next
                que.put((-prob_start[node_next], node_next))

    return prob_start[end]


if __name__ == "__main__":
    edges = [[0, 1], [1, 2], [0, 2]]
    succProb = [0.5, 0.5, 0.3]
    print(maxProbability(3, edges, succProb, 0, 2))
