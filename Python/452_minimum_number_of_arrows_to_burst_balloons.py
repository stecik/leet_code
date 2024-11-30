from typing import List

# original idea
# def findMinArrowShots(points: List[List[int]]) -> int:
#     arrows = 1
#     points.sort(key=lambda x: x[1])
#     i = 0
#     left = points[i][0]
#     right = points[i][1]
#     while i < len(points):
#         i += 1
#         if i == len(points):
#             break
#         left = max(left, points[i][0])
#         right = min(right, points[i][1])
#         if left > right:
#             arrows += 1
#             left = points[i][0]
#             right = points[i][1]
#     return arrows


# chatgpt speed optimization
# def findMinArrowShots(points: List[List[int]]) -> int:
#     if not points:
#         return 0
#     points.sort(key=lambda x: x[1])
#     arrows = 1
#     end = points[0][1]
#     for i in range(1, len(points)):
#         if points[i][0] > end:
#             arrows += 1
#             end = points[i][1]
#     return arrows


def findMinArrowShots(points: List[List[int]]) -> int:
    arrows = 1
    points.sort(key=lambda x: x[1])
    i = 1
    end = points[0][1]
    while i < len(points):
        if end < points[i][0]:
            arrows += 1
            end = points[i][1]
        i += 1
    return arrows


points = [[10, 16], [2, 8], [1, 6], [7, 12]]
print(findMinArrowShots(points))

points = [[1, 5], [1, 2], [6, 10], [5, 10]]
print(findMinArrowShots(points))

points = [[1, 2], [2, 3], [3, 4], [4, 5]]
print(findMinArrowShots(points))
