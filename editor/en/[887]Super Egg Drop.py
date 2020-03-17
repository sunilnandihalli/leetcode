# You are given K eggs, and you have access to a building with N floors from 1 t
# o N. 
# 
#  Each egg is identical in function, and if an egg breaks, you cannot drop it a
# gain. 
# 
#  You know that there exists a floor F with 0 <= F <= N such that any egg dropp
# ed at a floor higher than F will break, and any egg dropped at or below floor F 
# will not break. 
# 
#  Each move, you may take an egg (if you have an unbroken one) and drop it from
#  any floor X (with 1 <= X <= N). 
# 
#  Your goal is to know with certainty what the value of F is. 
# 
#  What is the minimum number of moves that you need to know with certainty what
#  F is, regardless of the initial value of F? 
# 
#  
# 
#  
#  
# 
#  
#  Example 1: 
# 
#  
# Input: K = 1, N = 2
# Output: 2
# Explanation: 
# Drop the egg from floor 1.  If it breaks, we know with certainty that F = 0.
# Otherwise, drop the egg from floor 2.  If it breaks, we know with certainty th
# at F = 1.
# If it didn't break, then we know with certainty F = 2.
# Hence, we needed 2 moves in the worst case to knhttps://old.reddit.com/ow what F is with certainty.
#  
# 
#  
#  Example 2: 
# 
#  
# Input: K = 2, N = 6
# Output: 3
#  
# 
#  
#  Example 3: 
# 
#  
# Input: K = 3, N = 14
# Output: 4
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= K <= 100 
#  1 <= N <= 10000 
#  
#  
#  
#  
#  Related Topics Math Binary Search Dynamic Programming
def test():
    ts = [(1, 2, 2), (2, 6, 3), (3, 14, 4)]
    for k, n, ans in ts:
        s = Solution()
        actual = s.superEggDrop(k, n)
        print(k, n, ans, actual)
        assert ans == actual


# leetcode submit region begin(Prohibit modification and deletion)
from functools import lru_cache
from math import sqrt


@lru_cache(None)
def f(n, e):
    if n == 0:
        return 0
    if e == 0:
        raise 'not possible'
    if n == 1:
        return 1
    if e == 1:
        return n
    return min([max(f(n - x, e), f(x - 1, e - 1)) + 1 for x in range(1, n)])


class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        for n in range(1, N + 1):
            for e in range(1, K + 1):
                f(n, e)
        return f(N, K)
# leetcode submit region end(Prohibit modification and deletion)
