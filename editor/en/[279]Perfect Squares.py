# Given a positive integer n, find the least number of perfect square numbers (f
# or example, 1, 4, 9, 16, ...) which sum to n. 
# 
#  Example 1: 
# 
#  
# Input: n = 12
# Output: 3 
# Explanation: 12 = 4 + 4 + 4. 
# 
#  Example 2: 
# 
#  
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9. Related Topics Math Dynamic Programming Breadth-first
#  Search
from functools import lru_cache
def ps_less_than(n):
    ret = []
    ps = 0
    addition = 1
    while ps < n:
        ps += addition
        addition+=2
        ret.append(ps)
    return ret

@lru_cache(None)
def lps(n):


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numSquares(self, n: int) -> int:
        
# leetcode submit region end(Prohibit modification and deletion)
