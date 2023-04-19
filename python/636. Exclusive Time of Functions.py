# https://leetcode.com/problems/exclusive-time-of-functions/


def exclusiveTime(n: int, logs: list[str]) -> list[int]:
    consump = [0] * n
    stack = []

    for log in logs:
        id, status, timestamp = log.split(":")
        id = int(id)
        timestamp = int(timestamp)
        if status == "start":
            stack.append([id, timestamp, 0])
        else:
            mid_time = 0
            while stack[-1][0] != id:
                pre_id, _, pre_time_used = stack.pop(-1)
                # consum[pre_id] += pre_time_used
                mid_time += pre_time_used
            consump[id] += timestamp - stack[-1][1] + 1 - mid_time
            stack[-1][2] = timestamp - stack[-1][1] + 1
            stack[-1][0] = -1

    return consump


if __name__ == "__main__":
    n = 1
    logs = [
        "0:start:0", "0:start:2", "0:end:5", "0:start:6", "0:end:6", "0:end:7"
    ]
    print(exclusiveTime(n, logs))
