# In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the
#  i-th domino. (A domino is a tile with two numbers from 1 to 6 - one on each hal
# f of the tile.) 
# 
#  We may rotate the i-th domino, so that A[i] and B[i] swap values. 
# 
#  Return the minimum number of rotations so that all the values in A are the sa
# me, or all the values in B are the same. 
# 
#  If it cannot be done, return -1. 
# 
#  
# 
#  Example 1: 
# 
#  
# 
#  
# Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
# Output: 2
# Explanation: 
# The first figure represents the dominoes as given by A and B: before we do any
#  rotations.
# If we rotate the second and fourth dominoes, we can make every value in the to
# p row equal to 2, as indicated by the second figure.
#  
# 
#  Example 2: 
# 
#  
# Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
# Output: -1
# Explanation: 
# In this case, it is not possible to rotate the dominoes to make one row of val
# ues equal.
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= A[i], B[i] <= 6 
#  2 <= A.length == B.length <= 20000 
#  
#  Related Topics Array Greedy
def test():
    ts = [([2, 1, 2, 4, 2, 2], [5, 2, 6, 2, 3, 2], 2), ([3, 5, 1, 2, 3], [3, 6, 3, 3, 4], -1)]
    for A, B, ans in ts:
        s = Solution()
        print(A, B)
        actual = s.minDominoRotations(A, B)
        print(A, B, ans, actual)
        assert ans == actual


from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
def swap(a, b, i):
    x = a[i]
    a[i] = b[i]
    b[i] = x


class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        i = 1
        n_swaps = 0
        A_equal = True
        B_equal = True
        while i < len(A):
            if A[i] == A[i - 1] or B[i] == B[i - 1]:
                i += 1
            elif A[i] == B[i - 1] or A[i - 1] == B[i]:
                n_swaps += 1
                swap(A, B, i)
                i += 1
            else:
                return -1
        return n_swaps

# leetcode submit region end(Prohibit modification and deletion)
