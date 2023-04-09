# https://leetcode.com/problems/combination-sum/


def combinationSum(candidates: list, target: int):
    ans = []
    candidates.sort()

    def binary_search(val: int, index: int):
        if val >= candidates[index]:
            return index
        l, r = 0, index
        while l < r:
            mid = (l + r) // 2
            if val >= candidates[mid] and val < candidates[mid + 1]:
                return mid
            elif val > candidates[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return l

    def findNext(val: int, index: int, comb: list):
        if val == 0:
            ans.append(comb)
            return
        if index < 0 or val < 2:
            return

        index = binary_search(val, index)

        for i in range(index, -1, -1):
            num_choice = val // candidates[i]
            for j in range(1, num_choice + 1):
                comb_cp = comb.copy()
                comb_cp = [candidates[i]] * j + comb_cp
                findNext(val - j * candidates[i], i - 1, comb_cp)

    findNext(target, len(candidates) - 1, [])

    return ans


if __name__ == "__main__":
    candidates = [2, 3, 6, 7]
    print(combinationSum(candidates, 7))
