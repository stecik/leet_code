from typing import List


def jump(nums: List[int]) -> int:
    jumps = 0
    i = 0
    while i < len(nums) - 1:
        k = 0
        max_reach = -1
        for j in range(1, min(nums[i] + 1, len(nums) - i)):
            if i + j == len(nums) - 1:
                return jumps + 1
            if nums[i + j] + j + i >= max_reach:
                k = i + j
                max_reach = nums[i + j] + j + i
        i = k
        jumps += 1
    return jumps


nums = [2, 3, 1, 1, 4]
print(jump(nums))

nums = [2, 1]
print(jump(nums))

nums = [1, 2, 3]
print(jump(nums))

nums = [3, 2, 1]
print(jump(nums))

nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 0]
print(jump(nums))

nums = [10, 10, 8, 7, 6, 5, 4, 3, 2, 1, 1, 0]
print(jump(nums))

nums = [2, 3, 1]
print(jump(nums))
