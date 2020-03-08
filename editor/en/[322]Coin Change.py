# You are given coins of different denominations and a total amount of money amo
# unt. Write a function to compute the fewest number of coins that you need to mak
# e up that amount. If that amount of money cannot be made up by any combination o
# f the coins, return -1. 
# 
#  Example 1: 
# 
#  
# Input: coins = [1, 2, 5], amount = 11
# Output: 3 
# Explanation: 11 = 5 + 5 + 1 
# 
#  Example 2: 
# 
#  
# Input: coins = [2], amount = 3
# Output: -1
#  
# 
#  Note: 
# You may assume that you have an infinite number of each kind of coin. 
#  Related Topics Dynamic Programming


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
# leetcode submit region end(Prohibit modification and deletion)
