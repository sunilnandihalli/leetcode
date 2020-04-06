# In an infinite chess board with coordinates from -infinity to +infinity, you h
# ave a knight at square [0, 0]. 
# 
#  A knight has 8 possible moves it can make, as illustrated below. Each move is
#  two squares in a cardinal direction, then one square in an orthogonal direction
# . 
# 
#  
# 
#  Return the minimum number of steps needed to move the knight to the square [x
# , y]. It is guaranteed the answer exists. 
# 
#  
#  Example 1: 
# 
#  
# Input: x = 2, y = 1
# Output: 1
# Explanation: [0, 0] → [2, 1]
#  
# 
#  Example 2: 
# 
#  
# Input: x = 5, y = 5
# Output: 4
# Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
#  
# 
#  
#  Constraints: 
# 
#  
#  |x| + |y| <= 300 
#  
#  Related Topics Breadth-first Search

def test():
    ts = [(2, 1, 1), (5, 5, 4)]
    for x, y, ans in ts:
        s = Solution()
        actual = s.minKnightMoves(x, y)
        assert actual == ans


# leetcode submit region begin(Prohibit modification and deletion)

from functools import lru_cache
import heapq as h


def moves(loc):
    x, y = loc
    for f in [1, -1]:
        for g in [1, -1]:
            for a, b in [(1, 2), (2, 1)]:
                yield (x + a * f, y + b * g)


def hdist(l1, l2):
    x1, y1 = l1
    x2, y2 = l2
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    return (dx ** 2 + dy ** 2) / 5


def mkm(target):
    start = (0, 0)
    num_steps_estimate = hdist(start, target)
    front = [(num_steps_estimate, 0, start)]
    in_front = set([start])
    while True:
        _, cur_steps, cur_loc = h.heappop(front)
        if cur_loc == target:
            return cur_steps
        for l in moves(cur_loc):
            if l not in in_front:
                h.heappush(front, (hdist(l, target) + cur_steps + 1, cur_steps + 1, l))


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        return mkm((x, y))
# leetcode submit region end(Prohibit modification and deletion)
