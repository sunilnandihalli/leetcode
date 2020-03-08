# Write an efficient algorithm that searches for a value in an m x n matrix. Thi
# s matrix has the following properties: 
# 
#  
#  Integers in each row are sorted in ascending from left to right. 
#  Integers in each column are sorted in ascending from top to bottom. 
#  
# 
#  Example: 
# 
#  Consider the following matrix: 
# 
#  
# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
#  
# 
#  Given target = 5, return true. 
# 
#  Given target = 20, return false. 
#  Related Topics Binary Search Divide and Conquer


# leetcode submit region begin(Prohibit modification and deletion)

def search(m, i1, j1, i2, j2, t):
    if i1 == i2 or j1 == j2:
        return False
    elif i1 + 1 == i2 and j1 + 1 == j2:
        return m[i1][j1] == t
    else:
        im = (i1 + i2) // 2
        jm = (j1 + j2) // 2
        if t < m[im][jm]:
            return search(m, i1, j1, im, jm, t) or search(m, im, j1, i2, jm, t) or search(m, i1, jm, im, j2, t)
        elif t > m[im][jm]:
            return search(m, im + 1, j1, i2, jm + 1, t) or search(m, im + 1, jm + 1, i2, j2, t) or search(m, i1, jm + 1,
                                                                                                          im + 1, j2, t)
        else:
            return True


class Solution:

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = matrix
        p = len(m)
        if p > 0:
            q = len(m[0])
        else:
            return False
        return search(m, 0, 0, p, q, target)
# leetcode submit region end(Prohibit modification and deletion)
