# Given a string s, partition s such that every substring of the partition is a 
# palindrome. 
# 
#  Return the minimum cuts needed for a palindrome partitioning of s. 
# 
#  Example: 
# 
#  
# Input: "aab"
# Output: 1
# Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 
# cut.
#  
#  Related Topics Dynamic Programming


# leetcode submit region begin(Prohibit modification and deletion)
from functools import lru_cache


def test():
    ts = [('', 0), ('b', 0), ('aba', 0), ('aab', 1), ('a', 0), ('abaab', 1), ('baaba', 1), ('abacaba', 0)]
    for s, ans in ts:
        sol = Solution()
        actual = sol.minCut(s)
        print(s, ans, actual)
        assert ans == actual


@lru_cache(None)
def mpc(s):
    if s == s[::-1]:
        m = 0
    else:
        m = len(s) - 1
        for i in range(1, len(s)):
            m = min(mpc(s[:i]) + mpc(s[i:]) + 1, m)
    return m


class Solution:
    def minCut(self, s: str) -> int:
        return mpc(s)
# leetcode submit region end(Prohibit modification and deletion)
