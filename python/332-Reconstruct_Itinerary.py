# https://leetcode.com/problems/reconstruct-itinerary/


def findItinerary(tickets: list):
    adj = dict()
    # first_visit = dict()

    for depart, destin in tickets:
        adj.setdefault(depart, [])
        adj[depart].append(destin)
        # first_visit.setdefault(depart, 301)

    for key in adj.keys():
        adj[key].sort()

    len_path = len(tickets)
    ans = None
    found = False

    def dfs(airport: str, step: int, cur_path: list):
        nonlocal ans, found
        cur_path.append(airport)

        if found:
            return

        if step == len_path:
            found = True
            ans = cur_path
            return

        for i in range(len(adj.setdefault(airport, []))):
            next = adj[airport].pop(0)
            dfs(next, step + 1, cur_path.copy())
            adj[airport].append(next)

    dfs("JFK", 0, [])
    return ans


if __name__ == "__main__":
    tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"],
               ["ATL", "SFO"]]
    print(findItinerary(tickets))
