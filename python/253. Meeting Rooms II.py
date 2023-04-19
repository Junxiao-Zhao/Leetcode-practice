# https://leetcode.ca/all/253.html


def minMeetingRooms(intervals):
    meetings = []

    for s, f in intervals:
        meetings.append([s, 0])
        meetings.append([f, 1])

    meetings.sort(key=lambda x: x[0])

    ans = 0
    count = 0
    for _, status in meetings:
        if not status:
            count += 1
        else:
            count -= 1
        ans = max(ans, count)

    return ans


if __name__ == "__main__":
    intervals = [[0, 30], [5, 10], [15, 20]]
    print(minMeetingRooms(intervals))
