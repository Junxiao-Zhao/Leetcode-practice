import bisect


class MyCalendarThree:

    def __init__(self):
        self.store = list()
        self.k = 1

    def book(self, startTime: int, endTime: int) -> int:
        p = [startTime, endTime]
        index = bisect.bisect(self.store, p)
        self.store.insert(index, p)

        i, j = index - 1, index + 1
        num = 1
        while i >= 0:
            if startTime >= self.store[i][0] and startTime < self.store[i][1]:
                num += 1
            else:
                break
            i -= 1
        while j < len(self.store):
            if endTime > self.store[j][0] and endTime <= self.store[j][1]:
                num += 1
            else:
                break
            j += 1

        self.k = max(self.k, num)
        return self.k


myCalendarThree = MyCalendarThree()
for i, j in [[24, 40], [43, 50], [27, 43], [5, 21], [30, 40], [14, 29],
             [3, 19], [3, 14], [25, 39], [6, 19]]:
    myCalendarThree.book(i, j)
