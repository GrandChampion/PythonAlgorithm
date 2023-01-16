# 253. Meeting Rooms II
# Interval partitioning problem from 4.1
from typing import List


def minMeetingRooms(intervals: List[List[int]]) -> int:
    start = sorted([interval[0] for interval in intervals])
    end = sorted([interval[1] for interval in intervals])

    maxLabel = 0
    label = 0

    startPosition = 0
    endPosition = 0

    while startPosition < len(intervals):
        if start[startPosition] < end[endPosition]:
            startPosition += 1
            label += 1
        else:
            endPosition += 1
            label -= 1
        maxLabel = max(maxLabel, label)
    return maxLabel
