from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = []
    start = intervals[0][0]
    end = intervals[0][1]
    for i in range(1, len(intervals)):
        if end < intervals[i][0]:
            merged.append([start, end])
            start = intervals[i][0]
            end = intervals[i][1]
        end = max(end, intervals[i][1])
    merged.append([start, end])
    return merged


# in-place solution (slower)
# def merge(intervals: List[List[int]]) -> List[List[int]]:
#     intervals.sort(key=lambda x: x[0])
#     i = 0
#     while i < len(intervals) - 1:
#         if (
#             intervals[i][1] >= intervals[i + 1][0]
#             and intervals[i][0] <= intervals[i + 1][1]
#         ):
#             intervals[i] = [
#                 min(intervals[i][0], intervals[i + 1][0]),
#                 max(intervals[i][1], intervals[i + 1][1]),
#             ]
#             intervals.pop(i + 1)
#         else:
#             i += 1
#     return intervals


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge(intervals))

intervals = [[1, 4], [2, 3]]
print(merge(intervals))

intervals = [[1, 4], [0, 2], [3, 5]]
print(merge(intervals))

intervals = []
print(merge(intervals))

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge(intervals))

intervals = [[1, 4], [0, 0]]
print(merge(intervals))
