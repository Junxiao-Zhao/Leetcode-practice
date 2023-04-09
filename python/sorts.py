# 两两交换，从后往前
def bubble_sort(nums: list) -> list:

    for i in range(0, len(nums) - 1):
        for j in range(0, len(nums) - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums


# unsort中最小和头交换，从前往后
def select_sort(nums: list) -> list:

    for i in range(0, len(nums)):
        min_index = i
        for j in range(i, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j

        if i != min_index:
            nums[i], nums[min_index] = nums[min_index], nums[j]

    return nums


# 将值往sorted中插入，从前往后
def insert_sort(nums: list) -> list:

    for i in range(1, len(nums)):
        while nums[i] < nums[i - 1]:
            nums[i], nums[i - 1] = nums[i - 1], nums[i]
            i -= 1

    return nums


def merge(left: list, right: list) -> list:

    result = list()

    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    if left:
        result += left
    elif right:
        result += right

    return result


def merge_sort(nums: list) -> list:
    if len(nums) < 2:
        return nums

    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)


def quick_sort(nums: list, left: int, right: int) -> list:

    if left < right:
        index = partition(nums, left, right)
        quick_sort(nums, left, index)
        quick_sort(nums, index + 1, right)

    return nums


def partition(nums: list, left: int, right: int) -> int:
    pivot = left
    i = j = left + 1

    while i <= right:
        if nums[i] < nums[pivot]:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1

        i += 1

    nums[pivot], nums[j - 1] = nums[j - 1], nums[pivot]
    return j - 1


if __name__ == "__main__":
    nums = [9, 11, 7, 3, 5, 4, 6, 2]
    print(bubble_sort(nums))
    print(select_sort(nums))
    print(insert_sort(nums))
    print(merge_sort(nums))
    print(quick_sort(nums, 0, len(nums) - 1))
