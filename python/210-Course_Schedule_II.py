# https://leetcode.com/problems/course-schedule-ii/


def findOrder(numCourses: int, prerequisites: list):
    if len(prerequisites) == 0:
        return [i for i in range(numCourses)]

    adj = dict()
    visited = [-1] * numCourses

    for a, b in prerequisites:
        adj.setdefault(a, [])
        adj[a].append(b)

    ans = []

    has_sol = True

    def dfs(course: int):
        nonlocal has_sol
        if not has_sol or visited[course] == 1:
            return
        elif visited[course] == 0:
            has_sol = False
            return

        visited[course] = 0
        for each in adj.setdefault(course, []):
            dfs(each)
        visited[course] = 1
        ans.append(course)

    for i in range(numCourses):
        if visited[i] == -1:
            dfs(i)
        if not has_sol:
            return []

    return ans


if __name__ == "__main__":
    print(findOrder(2, [[1, 0]]))
