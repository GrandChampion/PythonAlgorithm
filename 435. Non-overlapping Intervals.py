# 435. Non-overlapping Intervals
# Minimize the overlapping intervals to delete


from typing import List

interval1 = [[1, 2], [2, 3], [3, 4], [1, 3]]


def eraseOverlapIntervals(intervals: List[List[int]]) -> int:
    intervals.sort()
    removeCnt = 0
    previousEnd = intervals[0][1]

    for row in intervals[1:]:
        if (row[0] >= previousEnd):
            # Then skip: no deleting interval
            previousEnd = row[1]
        else:
            # If two intervals overlap: delete one interval that ends late
            previousEnd = min(row[1], previousEnd)
            removeCnt += 1

    return removeCnt


removedIntervals = eraseOverlapIntervals(interval1)
print(removedIntervals)
