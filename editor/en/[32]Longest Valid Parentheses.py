# Given a string containing just the characters '(' and ')', find the length of 
# the longest valid (well-formed) parentheses substring. 
# 
#  Example 1: 
# 
#  
# Input: "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()"
#  
# 
#  Example 2: 
# 
#  
# Input: ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()"
#  
#  Related Topics String Dynamic Programming

def test():
    ts = [('(()', 2), (')()())', 4), ('))((', 0), ('((((((()))))))', 14), (')(()()()()()())()()', 18), ('()', 2),
          ('()()', 4), ('(())', 4), ('()(())', 6), ('(()))())(', 4)]
    sol = Solution()
    for s, ans in ts:
        actual = sol.longestValidParentheses(s)
        print(s, ans, actual)
        assert actual == ans


# leetcode submit region begin(Prohibit modification and deletion)
from functools import lru_cache

openp = '('
closep = ')'


@lru_cache(None)
def lvp(s, i):  # lvp ending at i (including i)
    if i <= 0 or s[i] == openp:
        return 0
    if i - lvp(s, i - 1) - 1 > -1 and s[i - lvp(s, i - 1) - 1] == openp:
        return lvp(s, i - 1) + 2 + lvp(s, i - lvp(s, i - 1) - 2)
    else:
        return 0


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        m = 0
        for i in range(len(s)):
            m = max(lvp(s, i), m)
        return m
# leetcode submit region end(Prohibit modification and deletion)
