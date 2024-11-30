from typing import List


def summaryRanges(nums: List[int]) -> List[str]:
    if not nums:
        return []
    ranges = []
    i = 0
    j = 1
    while j < len(nums):
        if nums[j - 1] + 1 == nums[j]:
            j += 1
        else:
            ranges.append(f"{nums[i]}->{nums[j-1]}" if i != j - 1 else str(nums[i]))
            i = j
            j += 1
    ranges.append(f"{nums[i]}->{nums[j-1]}" if i != j - 1 else str(nums[i]))
    return ranges


nums = [0, 1, 2, 4, 5, 6]
print(summaryRanges(nums))

nums = [0, 1, 2, 4, 5, 7]
print(summaryRanges(nums))

nums = []
print(summaryRanges(nums))
