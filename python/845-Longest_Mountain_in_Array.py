# https://leetcode.com/problems/longest-mountain-in-array/


def longestMountain(arr: list):
    if len(arr) < 3:
        return 0

    i = 0
    count = 0
    while i + 2 < len(arr):
        if (arr[i - 1] >= arr[i] if i > 0 else True) and (arr[i + 1] > arr[i]):
            r = i + 1
            while (r < len(arr) and arr[r - 1] < arr[r]):
                r += 1
            if r < len(arr) and arr[r - 1] != arr[r]:
                while (r + 1 < len(arr) and arr[r + 1] < arr[r]):
                    r += 1

                if r < len(arr) and arr[r] < arr[r - 1] and (
                        arr[r] <= arr[r + 1] if r + 1 < len(arr) else True):
                    count = max(r - i + 1, count)
            i = r
        else:
            i += 1

    return count


if __name__ == "__main__":
    arr = [0, 0, 1, 0, 0, 1, 1, 1, 1, 1]
    print(longestMountain(arr))
