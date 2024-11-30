from typing import List


def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    if not intervals:
        return [newInterval]
    for i in range(len(intervals)):
        if newInterval[0] <= intervals[i][0]:
            intervals.insert(i, newInterval)
            if i < 2:
                return merge(intervals)
            return intervals[: i - 1] + merge(intervals[i - 1 :])
    intervals.append(newInterval)
    return intervals[:-2] + merge(intervals[-2:])


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


intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]
print(insert(intervals, newInterval))

intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval = [4, 8]
print(insert(intervals, newInterval))

intervals = [[1, 5]]
newInterval = [2, 3]
print(insert(intervals, newInterval))

intervals = [[1, 5]]
newInterval = [1, 7]
print(insert(intervals, newInterval))

intervals = [[1, 5]]
newInterval = [1, 2]
print(insert(intervals, newInterval))

intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]
print(insert(intervals, newInterval))
