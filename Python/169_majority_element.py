from typing import List


def majorityElement(nums: List[int]) -> int:
    count = 0
    candidate = None
    for item in nums:
        if candidate is None:
            candidate = item
            count = 1
        elif candidate == item:
            count += 1
        else:
            count -= 1
            if count == 0:
                candidate = None
    return candidate


nums = [3, 2, 2, 1, 1, 1, 2, 2, 2, 2, 2, 3]
print(majorityElement(nums))
