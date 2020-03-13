# Given strings S and T, find the minimum (contiguous) substring W of S, so that
#  T is a subsequence of W. 
# 
#  If there is no such window in S that covers all characters in T, return the e
# mpty string "". If there are multiple such minimum-length windows, return the on
# e with the left-most starting index. 
# 
#  Example 1: 
# 
#  
# Input: 
# S = "abcdebdde", T = "bde"
# Output: "bcde"
# Explanation: 
# "bcde" is the answer because it occurs before "bdde" which has the same length
# .
# "deb" is not a smaller window because the elements of T in the window must occ
# ur in order.
#  
# 
#  
# 
#  Note: 
# 
#  
#  All the strings in the input will only contain lowercase letters. 
#  The length of S will be in the range [1, 20000]. 
#  The length of T will be in the range [1, 100]. 
#  
# 
#  Related Topics Dynamic Programming Sliding Window

def test():
    ts = [('abcdebdde','bde','bcde'),('','abcd',''),('abcde','','')]
    for s,t,ans in ts:
        sol = Solution()
        actual = sol.minWindow(s,t)
        print(s,t,ans,actual)
        assert ans == actual

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minWindow(self, S: str, T: str) -> str:
        
# leetcode submit region end(Prohibit modification and deletion)
