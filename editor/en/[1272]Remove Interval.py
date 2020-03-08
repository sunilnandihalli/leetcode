# Given a sorted list of disjoint intervals, each interval intervals[i] = [a, b]
#  represents the set of real numbers x such that a <= x < b. 
# 
#  We remove the intersections between any interval in intervals and the interva
# l toBeRemoved. 
# 
#  Return a sorted list of intervals after all such removals. 
# 
#  
#  Example 1: 
#  Input: intervals = [[0,2],[3,4],[5,7]], toBeRemoved = [1,6]
# Output: [[0,1],[6,7]]
#  Example 2: 
#  Input: intervals = [[0,5]], toBeRemoved = [2,3]
# Output: [[0,2],[3,5]]
#  
#  
#  Constraints: 
# 
#  
#  1 <= intervals.length <= 10^4 
#  -10^9 <= intervals[i][0] < intervals[i][1] <= 10^9 
#  
#  Related Topics Math Line Sweep
from typing import List


def test():
    ts = [([[0, 2], [3, 4], [5, 7]], [1, 6], [[0, 1], [6, 7]]), ([[0, 5]], [2, 3], [[0, 2], [3, 5]]), (
    [[-995129934, -810666715], [-795583934, -695323316], [435891021, 802208428], [815898655, 883669821],
     [973099438, 982293900]], [-596926362, 285512274],
    [[-995129934, -810666715], [-795583934, -695323316], [435891021, 802208428], [815898655, 883669821],
     [973099438, 982293900]])]
    s = Solution()
    for intervals, toBeRemoved, ans in ts:
        actual = s.removeInterval(intervals, toBeRemoved)
        print(intervals, toBeRemoved, ans, actual)
        assert ans == actual


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        s, e = toBeRemoved
        i = 0
        ret = []
        while i < len(intervals) and intervals[i][1] < s:
            ret.append(intervals[i])
            i += 1

        if i < len(intervals) and intervals[i][0] < s:
            ret.append([intervals[i][0], s])

        while i < len(intervals) and intervals[i][1] < e:
            i += 1

        if i < len(intervals) and intervals[i][0] < e:
            ret.append([e, intervals[i][1]])
        i += 1

        while i < len(intervals):
            ret.append(intervals[i])
            i += 1

        return ret

# leetcode submit region end(Prohibit modification and deletion)
