# For some fixed N, an array A is beautiful if it is a permutation of the intege
# rs 1, 2, ..., N, such that: 
# 
#  For every i < j, there is no k with i < k < j such that A[k] * 2 = A[i] + A[j
# ]. 
# 
#  Given N, return any beautiful array A. (It is guaranteed that one exists.) 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: 4
# Output: [2,1,4,3]
#
# 
#  
#  Example 2: 
# 
#  
# Input: 5
# Output: [3,1,2,5,4] 
# 
#  
#  
# 
#  Note: 
# 
#  
#  1 <= N <= 1000 
#  
# 
#  
#  
#  Related Topics Divide and Conquer
from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
from functools import lru_cache
@lru_cache(1000)
def f(n):
    if n==1:
        return [1]
    return [2*x for x in f(n//2)] + [2*x-1 for x in f(n-n//2)]


class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        return f(N)
# leetcode submit region end(Prohibit modification and deletion)
