# A robot is located at the top-left corner of a m x n grid (marked 'Start' in t
# he diagram below). 
# 
#  The robot can only move either down or right at any point in time. The robot 
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in the d
# iagram below). 
# 
#  How many possible unique paths are there? 
# 
#  
# Above is a 7 x 3 grid. How many possible unique paths are there? 
# 
#  Note: m and n will be at most 100. 
# 
#  Example 1: 
# 
#  
# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the bottom-righ
# t corner:
# 1. Right -> Right -> Down
# 2. Right -> Down -> Right
# 3. Down -> Right -> Right
#  
# 
#  Example 2: 
# 
#  
# Input: m = 7, n = 3
# Output: 28 
#  Related Topics Array Dynamic Programming


# leetcode submit region begin(Prohibit modification and deletion)
from functools import lru_cache


@lru_cache(None)
def paths(i, j):
    if i == 0 or j == 0:
        return 1
    else:
        return paths(i, j - 1) + paths(i - 1, j)


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        for i in range(m):
            for j in range(n):
                paths(i, j)
        return paths(m - 1, n - 1)


@lru_cache(None)
def factorial(m):
    if m == 0:
        return 1

    return m * factorial(m - 1)


def num_paths(m, n):
    for i in range(m + n - 1):
        factorial(i)
    return factorial(m + n - 2) // (factorial(m - 1) * factorial(n - 1))


def test():
    ts = [(3, 2, 3), (7, 3, 28)]
    s = Solution()
    for m, n, ans in ts:
        assert num_paths(m, n) == ans
        assert s.uniquePaths(m, n) == ans
# leetcode submit region end(Prohibit modification and deletion)
