# We have two integer sequences A and B of the same non-zero length. 
# 
#  We are allowed to swap elements A[i] and B[i]. Note that both elements are in
#  the same index position in their respective sequences. 
# 
#  At the end of some number of swaps, A and B are both strictly increasing. (A 
# sequence is strictly increasing if and only if A[0] < A[1] < A[2] < ... < A[A.le
# ngth - 1].) 
# 
#  Given A and B, return the minimum number of swaps to make both sequences stri
# ctly increasing. It is guaranteed that the given input always makes it possible.
#  
# 
#  
# Example:
# Input: A = [1,3,5,4], B = [1,2,3,7]
# Output: 1
# Explanation: 
# Swap A[3] and B[3].  Then the sequences are:
# A = [1, 3, 5, 7] and B = [1, 2, 3, 4]
# which are both strictly increasing.
#  
# 
#  Note: 
# 
#  
#  A, B are arrays with the same length, and that length will be in the range [1
# , 1000]. 
#  A[i], B[i] are integer values in the range [0, 2000]. 
#  
#  Related Topics Dynamic Programming


# leetcode submit region begin(Prohibit modification and deletion)

def swap(A, B, i):
    tmp = A[i]
    A[i] = B[i]
    B[i] = tmp
from functools import lru_cache

@lru_cache(None)
def min_swap(A, B, i): # what is the minimum number of swaps necessary to make the lists A and B increasing upto i

    if i>0:
        if A[i]>A[i-1] and B[i]>B[i-1]:


    swap(A,B,i)
class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:

# leetcode submit region end(Prohibit modification and deletion)
