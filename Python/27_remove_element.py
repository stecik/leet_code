from typing import List


def removeElement(nums: List[int], val: int) -> int:
    i = 0
    j = 0
    k = 0
    while j < len(nums):
        if nums[j] == val:
            j += 1
        else:
            nums[i] = nums[j]
            i += 1
            k += 1
            j += 1
    return k


nums = [0, 3, 1, 0, 5, 0, 1, 0, 1, 2, 0, 3, 3, 0]
k = removeElement(nums, 0)
print(k, nums)
