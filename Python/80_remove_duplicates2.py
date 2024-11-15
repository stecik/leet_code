from typing import List


def removeDuplicates(nums: List[int]) -> int:
    k = 0
    i = 0
    j = 1
    counter = 1
    while j < len(nums):
        if nums[i] == nums[j]:
            if counter < 2:
                nums[i + 1] = nums[j]
                i += 1
                k += 1
                counter += 1
            else:
                j += 1
        else:
            counter = 1
            nums[i + 1] = nums[j]
            i += 1
            j += 1
            k += 1
    return k + 1


nums = [0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k = removeDuplicates(nums)
print(k, nums)

nums = [1, 1, 2]
k = removeDuplicates(nums)
print(k, nums)

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k = removeDuplicates(nums)
print(k, nums)
