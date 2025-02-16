from typing import List


def rob(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums)
    dp_min_1 = max(nums[0], nums[1])
    dp_min_2 = nums[0]
    for i in range(2, len(nums)):
        skip = dp_min_1
        rob = dp_min_2 + nums[i]
        dp_min_2 = dp_min_1
        dp_min_1 = max(skip, rob)
    return dp_min_1


nums = [1, 2, 3, 1]
print(rob(nums))

nums = [2, 7, 9, 3, 1]
print(rob(nums))

nums = [2, 1, 1, 2]
print(rob(nums))

nums = [8, 9, 8, 9, 8]
print(rob(nums))

nums = [8, 9, 8, 9, 1]
print(rob(nums))
