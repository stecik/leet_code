from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    k = m + n - 1
    while n > 0:
        if nums1[m - 1] < nums2[n - 1] or m == 0:
            nums1[k] = nums2[n - 1]
            n = n - 1
        else:
            nums1[k] = nums1[m - 1]
            nums1[m - 1] = 0
            m = m - 1
        k = k - 1

nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

nums1 = [0]
m = 0
nums2 = [1]
n = 1

nums1 = [1, 0]
m = 1
nums2 = [2]
n = 1

nums1 = [2, 0]
m = 1
nums2 = [1]
n = 1

merge(nums1, m, nums2, n)
print(nums1)
