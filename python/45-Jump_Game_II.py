# https://leetcode.com/problems/jump-game-ii/


def jump(nums: list):
    if len(nums) <= 1:
        return 0
    i = j = count = 0
    local_max = -1
    next_visited = 1

    while i < len(nums):
        if nums[i] >= len(nums) - i - 1:
            count += 1
            break
        for k in range(next_visited, i + nums[i] + 1):
            if k + nums[k] >= local_max:
                j = k
                local_max = k + nums[k]

        next_visited = i + nums[i] + 1
        i = j
        local_max = -1
        count += 1

    return count


if __name__ == "__main__":
    nums = [1, 1, 1, 1]
    print(jump(nums))
