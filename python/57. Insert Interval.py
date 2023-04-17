# https://leetcode.com/problems/insert-interval/


def insert(intervals: list[list[int]],
           newInterval: list[int]) -> list[list[int]]:

    if not intervals:
        return [newInterval]

    l, r = 0, len(intervals) - 1

    while l < r:
        mid = int(l + (r - l + 1) / 2)

        if intervals[mid][0] <= newInterval[0]:
            l = mid
        else:
            r = mid - 1

    if newInterval[0] > intervals[l][0]:
        intervals.insert(l + 1, newInterval)
    else:
        intervals.insert(l, newInterval)

    i = l
    while i < len(intervals) - 1:
        cur = intervals[i]
        next = intervals[i + 1]
        if cur[0] > newInterval[1]:
            break
        if cur[1] >= next[0]:
            intervals[i][1] = max(intervals[i][1], intervals[i + 1][1])
            intervals.pop(i + 1)
        else:
            i += 1

    return intervals


if __name__ == "__main__":
    intervals = [[1, 5]]
    newInterval = [0, 3]
    print(insert(intervals, newInterval))
