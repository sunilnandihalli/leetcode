# Given a list of intervals, remove all intervals that are covered by another in
# terval in the list. Interval [a,b) is covered by interval [c,d) if and only if c
#  <= a and b <= d. 
# 
#  After doing so, return the number of remaining intervals. 
# 
#  
#  Example 1: 
# 
#  
# Input: intervals = [[1,4],[3,6],[2,8]]
# Output: 2
# Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= intervals.length <= 1000 
#  0 <= intervals[i][0] < intervals[i][1] <= 10^5 
#  intervals[i] != intervals[j] for all i != j 
#  
#  Related Topics Line Sweep
from typing import List

# leetcode submit region begin(Prohibit modification and deletion)

import heapq as h


def rci(intervals):
    intervals = sorted(intervals, key=lambda x: (x[0], -x[1]))
    ret = []
    i = 0
    while i < len(intervals):
        s, e = intervals[i]
        i += 1
        while i < len(intervals) and intervals[i][1] <= e:
            i += 1
        ret.append([s, e])
    return ret


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        return len(rci(intervals))


# leetcode submit region end(Prohibit modification and deletion)
def test():
    ts = [([[1, 4], [3, 6], [2, 8]], 2)]
    sol = Solution()
    for intervals, ans in ts:
        actual = sol.removeCoveredIntervals(intervals)
        print(intervals, ans, actual)
        assert actual == ans
