# Given an array of meeting time intervals consisting of start and end times [[s
# 1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms requir
# ed. 
# 
#  Example 1: 
# 
#  
# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2 
# 
#  Example 2: 
# 
#  
# Input: [[7,10],[2,4]]
# Output: 1 
# 
#  NOTE: input types have been changed on April 15, 2019. Please reset to defaul
# t code definition to get new method signature. 
#  Related Topics Heap Greedy Sort


# leetcode submit region begin(Prohibit modification and deletion)
import heapq as h

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)
        i = 0
        end_points = []
        minMeetingRooms = 0
        while i < len(intervals):
            s, e = intervals[i]
            while len(end_points) > 0 and s >= end_points[0]:
                h.heappop(end_points)
            h.heappush(end_points, e)
            if minMeetingRooms < len(end_points):
                minMeetingRooms = len(end_points)
            i += 1
        return minMeetingRooms
# leetcode submit region end(Prohibit modification and deletion)
