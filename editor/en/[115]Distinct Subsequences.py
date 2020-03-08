# Given a string S and a string T, count the number of distinct subsequences of 
# S which equals T. 
# 
#  A subsequence of a string is a new string which is formed from the original s
# tring by deleting some (can be none) of the characters without disturbing the re
# lative positions of the remaining characters. (ie, "ACE" is a subsequence of "AB
# CDE" while "AEC" is not). 
# 
#  Example 1: 
# 
#  
# Input: S = "rabbbit", T = "rabbit"
# Output: 3
# Explanation:
# 
# As shown below, there are 3 ways you can generate "rabbit" from S.
# (The caret symbol ^ means the chosen letters)
# 
# rabbbit
# ^^^^ ^^
# rabbbit
# ^^ ^^^^
# rabbbit
# ^^^ ^^^
#  
# 
#  Example 2: 
# 
#  
# Input: S = "babgbag", T = "bag"
# Output: 5
# Explanation:
# 
# As shown below, there are 5 ways you can generate "bag" from S.
# (The caret symbol ^ means the chosen letters)
# 
# babgbag
# ^^ ^
# babgbag
# ^^    ^
# babgbag
# ^    ^^
# babgbag
#   ^  ^^
# babgbag
#     ^^^
#  
#  Related Topics String Dynamic Programming


# leetcode submit region begin(Prohibit modification and deletion)
from functools import lru_cache


def test():
    ts = [('rabbbit', 'rabbit', 3), ('babgbag', 'bag', 5)]
    sol = Solution()
    for s, t, ans in ts:
        actual = sol.numDistinct(s, t)
        print(s, t, ans, actual)
        assert actual == ans
        
@lru_cache(None)
def num_distinct(s,t,i,j):
    if j==len(t):
        return 1
    elif i==len(s) and j<len(t):
        return 0
    elif s[i]==t[j]:
        return num_distinct(s,t,i+1,j+1)+num_distinct(s,t,i+1,j)
    else:
        return num_distinct(s,t,i+1,j)
        

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        for i in range(len(s)-1,-1,-1):
            for j in range(len(t)-1,-1,-1):
                num_distinct(s,t,i,j)
        return num_distinct(s,t,0,0)
# leetcode submit region end(Prohibit modification and deletion)
