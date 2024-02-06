import heapq

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # Intuition: Sort the intervals by start time
        # Use min-heap to track of available rooms
        # Iterate through each sorted interval
        # 1) For each iteration, pop and update new root value if
        # root value which is end time of meeting <= new start time 
        # 2) Or, just push the new start time to the heap increasing heap size 
        # by 1 (When new start time < prev end time)
        intervals.sort(key = lambda i:i.start)
        rooms = [intervals[0].end]
        heapq.heapify(rooms)
        for i in range(1,len(intervals)):
            if rooms[0] <= intervals[i].start:
                heapq.heappushpop(rooms, intervals[i].end)
            else:
                heapq.heappush(rooms, intervals[i].end)
        return len(rooms)