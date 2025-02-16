from typing import List
from bisect import bisect_left

# slow
# def threeSum(nums: List[int]) -> List[List[int]]:
#     nums.sort()
#     res = set()
#     i = 0
#     while i < len(nums) - 2:
#         target = -nums[i]
#         j = i + 1
#         k = len(nums) - 1
#         while j < k:
#             if nums[j] + nums[k] == target:
#                 if i != j != k:
#                     res.add((nums[i], nums[j], nums[k]))
#                 j += 1
#                 k -= 1
#             elif nums[j] + nums[k] < target:
#                 j += 1
#             else:
#                 k -= 1
#         i += 1
#     return list(res)


# faster
# def threeSum(nums: List[int]) -> List[List[int]]:
#     new_nums = []
#     freq_table = {}
#     for num in nums:
#         if num in freq_table:
#             freq_table[num] += 1
#         else:
#             freq_table[num] = 1

#         count = freq_table[num]
#         if count <= 2:
#             new_nums.append(num)
#         elif count <= 3 and num == 0:
#             new_nums.append(num)

#     nums = sorted(new_nums)
#     res = set()
#     i = 0
#     while i < len(nums) - 2:
#         target = -nums[i]
#         j = i + 1
#         k = len(nums) - 1
#         while j < k:
#             if nums[j] + nums[k] == target:
#                 if i != j != k:
#                     res.add((nums[i], nums[j], nums[k]))
#                 j += 1
#                 k -= 1
#             elif nums[j] + nums[k] < target:
#                 j += 1
#             else:
#                 k -= 1
#         i += 1
#     return list(res)

# faster with skipping duplicates
# def threeSum(nums: List[int]) -> List[List[int]]:
#     nums.sort()
#     res = set()
#     i = 0
#     while i < len(nums) - 2:
#         target = -nums[i]
#         j = i + 1
#         k = len(nums) - 1
#         while j < k:
#             if nums[j] + nums[k] == target:
#                 while j + 1 < k - 1 and nums[j] == nums[j + 1]:
#                     j += 1
#                 while j + 1 < k - 1 and nums[k] == nums[k - 1]:
#                     k -= 1
#                 if i != j != k:
#                     res.add((nums[i], nums[j], nums[k]))
#                 j += 1
#                 k -= 1
#             elif nums[j] + nums[k] < target:
#                 j += 1
#             else:
#                 k -= 1
#         if i + 1 < len(nums) - 2 and nums[i] == nums[i + 1]:
#             while i + 1 < len(nums) - 2 and nums[i] == nums[i + 1]:
#                 i += 1
#         else:
#             i += 1
#     return list(res)


# chatgpt optimization
def threeSum(nums: List[int]) -> List[List[int]]:
    res = []
    new_nums = []
    freq_table = {}
    for num in nums:
        if num in freq_table:
            freq_table[num] += 1
        else:
            freq_table[num] = 1
    freq_table = {key: freq_table[key] for key in sorted(freq_table)}

    if 0 in freq_table:
        if freq_table[0] >= 3:
            res.append([0, 0, 0])
        del freq_table[0]
        for key in freq_table:
            if key >= 0:
                break
            if -key in freq_table:
                res.append([-key, 0, key])

    for key in freq_table:
        val = freq_table[key]
        new_nums.append(key)
        if val >= 2 and key != 0:
            diff = -2 * key
            if diff in freq_table:
                res.append([key, key, diff])
    nums = new_nums
    n = len(nums)
    for i in range(n - 2):
        # Skip duplicate values for the first number
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        target = -nums[i]
        j, k = i + 1, n - 1
        while j < k:
            current_sum = nums[j] + nums[k]
            if current_sum == target:
                res.append([nums[i], nums[j], nums[k]])

                # Skip duplicates for the second and third numbers
                while j < k and nums[j] == nums[j + 1]:
                    j += 1
                while j < k and nums[k] == nums[k - 1]:
                    k -= 1

                # Move both pointers inward
                j += 1
                k -= 1
            elif current_sum < target:
                j += 1
            else:
                k -= 1
    return res


nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))

nums = [0, 1, 1]
print(threeSum(nums))

nums = [0, 0, 0]
print(threeSum(nums))

nums = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1]
print(threeSum(nums))

nums = [-1, 0, 1, 0]
print(threeSum(nums))

nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))

nums = [0, 0, 0]
print(threeSum(nums))

nums = [-4, -2, 1, -5, -4, -4, 4, -2, 0, 4, 0, -2, 3, 1, -5, 0]
print(threeSum(nums))
