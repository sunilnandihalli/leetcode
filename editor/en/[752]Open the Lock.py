# 
# You have a lock in front of you with 4 circular wheels. Each wheel has 10 slot
# s: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freel
# y and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each
#  move consists of turning one wheel one slot.
#  
# The lock initially starts at '0000', a string representing the state of the 4 
# wheels.
#  
# You are given a list of deadends dead ends, meaning if the lock displays any o
# f these codes, the wheels of the lock will stop turning and you will be unable t
# o open it.
#  
# Given a target representing the value of the wheels that will unlock the lock,
#  return the minimum total number of turns required to open the lock, or -1 if it
#  is impossible.
#  
# 
#  Example 1: 
#  
# Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
# Output: 6
# Explanation:
# A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "12
# 01" -> "1202" -> "0202".
# Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would
#  be invalid,
# because the wheels of the lock become stuck after the display becomes the dead
#  end "0102".
#  
#  
# 
#  Example 2: 
#  
# Input: deadends = ["8888"], target = "0009"
# Output: 1
# Explanation:
# We can turn the last wheel in reverse to move from "0000" -> "0009".
#  
#  
# 
#  Example 3: 
#  
# Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], t
# arget = "8888"
# Output: -1
# Explanation:
# We can't reach the target without getting stuck.
#  
#  
# 
#  Example 4: 
#  
# Input: deadends = ["0000"], target = "8888"
# Output: -1
#  
#  
# 
#  Note: 
#  
#  The length of deadends will be in the range [1, 500]. 
#  target will not be in the list deadends. 
#  Every string in deadends and the string target will be a string of 4 digits f
# rom the 10,000 possibilities '0000' to '9999'. 
#  
#  Related Topics Breadth-first Search
from typing import List


def test():
    ts = [(["0201", "0101", "0102", "1212", "2002"], "0202", 6),
          (['8888'], '0009', 1),
          (["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], '8888', -1),
          (['0000'], '8888', -1)]
    for deadends, target, ans in ts:
        s = Solution()
        actual = s.openLock(deadends, target)
        print(deadends, target, ans, actual)
        assert actual == ans


# leetcode submit region begin(Prohibit modification and deletion)
import heapq as h


def dist(cur, target):
    ret = 0
    for x, y in zip(cur, target):
        x = int(x)
        y = int(y)
        ret += min(abs(x - y), 10 + x - y)
    return ret


def options(cur):
    for i, x in enumerate(cur):
        for d in [1, -1]:
            yield cur[:i] + str((10 + int(x) + d) % 10) + cur[i + 1:]


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        s = '0000'
        if s in deadends:
            return -1
        front = [(dist(s, target), 0, s)]
        visited = set([s])
        while len(front) > 0:
            _, dist_to_cur, cur = h.heappop(front)
            if cur == target:
                return dist_to_cur
            for nxt in options(cur):
                if nxt not in deadends and nxt not in visited:
                    h.heappush(front, (dist(nxt, target) + dist_to_cur + 1, dist_to_cur + 1, nxt))
                    visited.add(nxt)
        return -1
# leetcode submit region end(Prohibit modification and deletion)
