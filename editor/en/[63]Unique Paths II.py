# A robot is located at the top-left corner of a m x n grid (marked 'Start' in t
# he diagram below). 
# 
#  The robot can only move either down or right at any point in time. The robot 
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in the d
# iagram below). 
# 
#  Now consider if some obstacles are added to the grids. How many unique paths 
# would there be? 
# 
#  
# 
#  An obstacle and empty space is marked as 1 and 0 respectively in the grid. 
# 
#  Note: m and n will be at most 100. 
# 
#  Example 1: 
# 
#  
# Input:
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# Output: 2
# Explanation:
# There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
#  
#  Related Topics Array Dynamic Programming


# leetcode submit region begin(Prohibit modification and deletion)
from functools import lru_cache


class Solution:
    @lru_cache(None)
    def paths(self, i, j):
        if i < 0 or j < 0:
            return 0
        elif self.m[i][j] == 1:
            return 0
        elif i == 0 and j == 0:
            return 1
        else:
            return self.paths(i - 1, j) + self.paths(i, j - 1)

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        p = len(obstacleGrid)
        q = len(obstacleGrid[0]) if p > 0 else 0

        self.m = obstacleGrid
        for i in range(p):
            for j in range(q):
                self.paths(i, j)
        return self.paths(p - 1, q - 1)

# leetcode submit region end(Prohibit modification and deletion)
