# You are climbing a stair case. It takes n steps to reach to the top. 
# 
#  Each time you can either climb 1 or 2 steps. In how many distinct ways can yo
# u climb to the top? 
# 
#  Note: Given n will be a positive integer. 
# 
#  Example 1: 
# 
#  
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
#  
# 
#  Example 2: 
# 
#  
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#  
#  Related Topics Dynamic Programming

def test():
    ts = [(2,2),(3,3)]
    s = Solution()
    for n,ans in ts:
        assert ans == s.climbStairs(n)

# leetcode submit region begin(Prohibit modification and deletion)
from functools import lru_cache


@lru_cache(None)
def stairs(n):
    if n<0:
        return 0
    elif n==0:
        return 1
    else:
        return stairs(n-1)+stairs(n-2)
class Solution:
    def climbStairs(self, n: int) -> int:
        for i in range(n):
            stairs(i)
        return stairs(n)

# leetcode submit region end(Prohibit modification and deletion)
