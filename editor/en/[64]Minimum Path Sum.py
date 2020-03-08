# Given a m x n grid filled with non-negative numbers, find a path from top left
#  to bottom right which minimizes the sum of all numbers along its path. 
# 
#  Note: You can only move either down or right at any point in time. 
# 
#  Example: 
# 
#  
# Input:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.
#  
#  Related Topics Array Dynamic Programming


# leetcode submit region begin(Prohibit modification and deletion)
from functools import lru_cache


class Solution:
    @lru_cache(None)
    def pcost(self, i, j):
        if i < 0 or j < 0:
            return float('inf')
        elif i == 0 and j == 0:
            return self.m[i][j]
        else:
            return min(self.pcost(i - 1, j), self.pcost(i, j - 1)) + self.m[i][j]

    def minPathSum(self, grid: List[List[int]]) -> int:
        self.m = grid
        p = len(grid)
        q = len(grid[0]) if p > 0 else 0
        for i in range(p):
            for j in range(q):
                self.pcost(i, j)
        return self.pcost(p - 1, q - 1)
# leetcode submit region end(Prohibit modification and deletion)
