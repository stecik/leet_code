from typing import List


def maxArea(height: List[int]) -> int:
    max_area = 0
    max_height = max(height)
    left = 0
    right = len(height) - 1
    while left < right:
        max_area = max(max_area, min(height[left], height[right]) * (right - left))
        if max_area >= max_height * (right - left - 1):
            break
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(height))

height = [2, 3, 4, 5, 18, 17, 6]
print(maxArea(height))
