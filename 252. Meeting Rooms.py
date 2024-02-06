"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        #Intuition: Sort the intervals's start time
        #Since we are working with data structure we created: Interval
        #We must use intervals.sort(key = lambda i:i.start) which sorts
        # the list by i.start of all intervals
        intervals.sort(key=lambda i: i.start)
        for i in range(1, len(intervals)):
            # Must make sure the end time of previous interval
            # Doesn't interfere with the start time of next interval
            if intervals[i - 1].end > intervals[i].start:
                return False
        return True
