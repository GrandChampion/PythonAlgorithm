from typing import List


def canAttendMeetings(intervals: List[List[int]]) -> bool:
    # Check if interval is empty
    if (intervals == []):
        return True
    intervals.sort()
    previousEnd = intervals[0][1]
    for interval in intervals[1:]:
        if interval[0] >= previousEnd:
            previousEnd = interval[1]
        else:
            return False
    return True


interval1 = [[1, 2], [2, 3], [2, 4]]
print(canAttendMeetings(interval1))
