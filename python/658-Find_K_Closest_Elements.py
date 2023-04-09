# https://leetcode.com/problems/find-k-closest-elements/


def findClosestElements(arr: list, k: int, x: int):

    def binary(target: int):
        l, r = 0, len(arr) - 1
        while l < r:
            mid = (l + r) // 2
            if arr[mid] == x or (
                    arr[mid] < x and
                (arr[mid + 1] > x if mid + 1 < len(arr) - 1 else True)):
                return mid
            elif arr[mid] < x:
                l = mid + 1
            else:
                r = mid - 1
        return l

    start = binary(x)
    ans = []
    l, r = start, start + 1
    while k > 0:
        if r >= len(arr) or abs(arr[l] - x) <= abs(arr[r] - x):
            ans.append(arr[l])
            l -= 1
        else:
            ans.append(arr[r])
            r += 1
        k -= 1

    return list(sorted(ans))


if __name__ == "__main__":
    arr = [1, 1, 1, 10, 10, 10]
    print(findClosestElements(arr, 1, 9))
