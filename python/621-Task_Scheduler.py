# https://leetcode.com/problems/task-scheduler/


def leastInterval(tasks: list, n: int):
    from queue import PriorityQueue

    count = dict()
    for each in tasks:
        count.setdefault(each, 0)
        count[each] += 1

    que = PriorityQueue()
    for key, val in count.items():
        que.put((-val, key))

    pending = []
    time = 0

    while que.qsize() or len(pending):
        if len(pending) and pending[0][0] <= time:
            _, rest_num, pending_name = pending.pop(0)
            que.put((-rest_num, pending_name))

        if que.qsize():
            num, task_name = que.get()
            if -num - 1 > 0:
                pending.append((time + n + 1, -num - 1, task_name))

        time += 1

    return time


if __name__ == "__main__":
    tasks = ["A", "A", "A", "B", "B", "B"]
    print(leastInterval(tasks, 2))
