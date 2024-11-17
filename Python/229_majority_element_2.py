from typing import List
import array
from math import log, e, ceil, floor

# CMS
# def majorityElement(nums: List[int]) -> List[int]:
#     cms = CountMinSketch(0.09, 0.3)
#     for item in nums:
#         cms.update(item)
#     return [item for item in set(nums) if cms.estimate(item) > floor(len(nums) / 3)]


# class CountMinSketch:
#     def __init__(self, eps, delta):
#         self.eps = eps
#         self.delta = delta
#         self.w = int(ceil(e / eps))
#         self.d = int(ceil(log(1.0 / delta)))
#         self.sketch = [array.array("h", [0] * self.w) for _ in range(self.d)]

#     def _hash(self, item, seed):
#         return hash(item) ^ (seed * 31)

#     def update(self, item, freq=1):
#         for i in range(self.d):
#             index = self._hash(item, i) % self.w
#             self.sketch[i][index] += freq

#     def estimate(self, item):
#         return int(
#             min(self.sketch[i][self._hash(item, i) % self.w] for i in range(self.d))
#         )


def majorityElement(nums: List[int]) -> List[int]:
    k = 3
    candidates = dict()
    for item in nums:
        if item in candidates.keys():
            candidates[item] += 1
        elif len(candidates) < k - 1:
            candidates[item] = 1
        else:
            candidates = {key: val - 1 for key, val in candidates.items() if val > 1}
    return [item for item in candidates.keys() if nums.count(item) > len(nums) // k]


nums = [3, 2, 3]
print(majorityElement(nums))

nums = [1]
print(majorityElement(nums))

nums = [1, 2]
print(majorityElement(nums))

nums = [6, 4, 5, 5, 4, 4, 4]
print(majorityElement(nums))

nums = [2, 2]
print(majorityElement(nums))

nums = [2, 2, 1, 3]
print(majorityElement(nums))
