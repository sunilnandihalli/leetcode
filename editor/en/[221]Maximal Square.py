# Given a 2D binary matrix filled with 0's and 1's, find the largest square cont
# aining only 1's and return its area. 
# 
#  Example: 
# 
#  
# Input: 
# 
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# 
# Output: 4
#  Related Topics Dynamic Programming


# leetcode submit region begin(Prohibit modification and deletion)
from functools import lru_cache


@lru_cache(None)
def num_ones(m, i, j):
    if i < 0 or j < 0:
        return 0
    else:
        return num_ones(m, i - 1, j) + num_ones(m, i, j - 1) - num_ones(m, i - 1, j - 1) + 1 if m[i][j] == '1' else 0


def num_ones_square(m, i, j, l):
    return num_ones(m, i, j) - num_ones(m, i - l, j) - num_ones(m, i, j - l) + num_ones(m, i - l, j - l)


def is_square(m, i, j, l):
    return num_ones_square(m, i, j, l) == l * l


@lru_cache(None)
def height_of_ones(m, i, j):
    if i < 0 or m[i][j] == '0':
        return 0
    else:
        return height_of_ones(m, i - 1, j) + 1


@lru_cache(None)
def width_of_ones(m, i, j):
    if j < 0 or m[i][j] == '0':
        return 0
    else:
        return width_of_ones(m, i, j - 1) + 1


@lru_cache(None)
def largest_square(m, i, j):
    if i < 0 or j < 0 or m[i][j] == '0':
        return 0
    else:
        l1 = largest_square(m, i - 1, j - 1)
        return min([width_of_ones(m, i, j), height_of_ones(m, i, j), l1 + 1])


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        p = len(matrix)
        q = len(matrix[0]) if p > 0 else 0
        m = tuple([''.join(x) for x in matrix])
        largest_square_length = 0
        for i in range(p):
            for j in range(q):
                largest_square_length = max(largest_square(m, i, j), largest_square_length)
        return largest_square_length * largest_square_length
# leetcode submit region end(Prohibit modification and deletion)
