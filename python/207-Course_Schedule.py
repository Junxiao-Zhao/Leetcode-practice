# https://leetcode.com/problems/course-schedule/


def canFinish(numCourses: int, prerequisites: list):
    if len(prerequisites) == 0:
        return True

    adj = dict()
    visited = dict()
    for course, pre in prerequisites:
        adj.setdefault(course, [])
        adj[course].append(pre)

    for i in range(numCourses):
        visited.setdefault(i, -1)

    finish = True

    def dfs(course: int):
        nonlocal finish

        if visited[course] == 1 or not finish:
            return

        if visited[course] == 0:
            finish = False
            return

        visited[course] = 0
        for each in adj.setdefault(course, []):
            dfs(each)
        visited[course] = 1

    for i in range(numCourses):
        if not finish:
            return finish
        if visited[i] == -1:
            dfs(i)

    return finish
