# Given a positive integer n, return the number of all possible attendance recor
# ds with length n, which will be regarded as rewardable. The answer may be very l
# arge, return it after mod 109 + 7. 
# 
#  A student attendance record is a string that only contains the following thre
# e characters: 
# 
#  
#  
#  'A' : Absent. 
#  'L' : Late. 
#  'P' : Present. 
#  
#  
# 
#  
# A record is regarded as rewardable if it doesn't contain more than one 'A' (ab
# sent) or more than two continuous 'L' (late). 
# 
#  Example 1: 
#  
# Input: n = 2
# Output: 8 
# Explanation:
# There are 8 records with length 2 will be regarded as rewardable:
# "PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
# Only "AA" won't be regarded as rewardable owing to more than one absent times.
#  
#  
#  
# 
#  Note:
# The value of n won't exceed 100,000.
#  
# 
# 
#  Related Topics Dynamic Programming

def test():
    ts = [(2, 8),(4,43)]
    for x, ans in ts:
        s = Solution()
        actual = s.checkRecord(x)
        assert ans == actual

def formula(n):
    return 1 + n * 2 + (n * (n - 1)) // 2 + n * (n - 1) + (n * (n - 1) * (n - 2)) // 2

def dp(n):

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def checkRecord(self, n: int) -> int:


# leetcode submit region end(Prohibit modification and deletion)
