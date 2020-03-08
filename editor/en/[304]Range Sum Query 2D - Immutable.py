# Given a 2D matrix matrix, find the sum of the elements inside the rectangle de
# fined by its upper left corner (row1, col1) and lower right corner (row2, col2).
#  
# 
#  
#  
# The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) 
# and (row2, col2) = (4, 3), which contains sum = 8.
#  
# 
#  Example: 
#  
# Given matrix = [
#   [3, 0, 1, 4, 2],
#   [5, 6, 3, 2, 1],
#   [1, 2, 0, 1, 5],
#   [4, 1, 0, 1, 7],
#   [1, 0, 3, 0, 5]
# ]
# 
# sumRegion(2, 1, 4, 3) -> 8
# sumRegion(1, 1, 2, 2) -> 11
# sumRegion(1, 2, 2, 4) -> 12
#  
#  
# 
#  Note: 
#  
#  You may assume that the matrix does not change. 
#  There are many calls to sumRegion function. 
#  You may assume that row1 ≤ row2 and col1 ≤ col2. 
#  
#  Related Topics Dynamic Programming
from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        p = len(matrix)
        q = len(matrix[0]) if p > 0 else 0
        self.matrix = matrix
        m = self.matrix
        for i in range(p):
            for j in range(q):
                s = m[i][j]
                if i > 0:
                    s += m[i - 1][j]
                if j > 0:
                    s += m[i][j - 1]
                if i > 0 and j > 0:
                    s -= m[i - 1][j - 1]
                m[i][j] = s

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        m = self.matrix
        return m[row2][col2] - (m[row2][col1 - 1] if col1 > 0 else 0) - (m[row1 - 1][col2] if row1 > 0 else 0) + (
            m[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0)

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# leetcode submit region end(Prohibit modification and deletion)
