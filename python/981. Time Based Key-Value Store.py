from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.store = defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        t_v = self.store[key]
        target = t_v.get(timestamp, None)

        if target is not None:
            return target

        t_v = list(t_v.items())

        return self.binary_search(t_v, timestamp)

    def binary_search(self, item: list, timestamp: int) -> str:
        l = 0
        r = len(item) - 1

        while l <= r:
            mid = (l + r) // 2

            if (item[mid][0] <= timestamp):
                l = mid + 1
            else:
                r = mid - 1

        return item[r][1] if r >= 0 else ""


if __name__ == "__main__":
    tm = TimeMap()
    tm.set("foo", "bar", 1)
    print(tm.get("foo", 1))
    print(tm.get("foo", 3))
    tm.set("foo", "bar2", 4)
    print(tm.get("foo", 4))
    print(tm.get("foo", 5))
