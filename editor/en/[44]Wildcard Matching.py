# Given an input string (s) and a pattern (p), implement wildcard pattern matchi
# ng with support for '?' and '*'. 
# 
#  
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
#  
# 
#  The matching should cover the entire input string (not partial). 
# 
#  Note: 
# 
#  
#  s could be empty and contains only lowercase letters a-z. 
#  p could be empty and contains only lowercase letters a-z, and characters like
#  ? or *. 
#  
# 
#  Example 1: 
# 
#  
# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
#  
# 
#  Example 2: 
# 
#  
# Input:
# s = "aa"
# p = "*"
# Output: true
# Explanation: '*' matches any sequence.
#  
# 
#  Example 3: 
# 
#  
# Input:
# s = "cb"
# p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not mat
# ch 'b'.
#  
# 
#  Example 4: 
# 
#  
# Input:
# s = "adceb"
# p = "*a*b"
# Output: true
# Explanation: The first '*' matches the empty sequence, while the second '*' ma
# tches the substring "dce".
#  
# 
#  Example 5: 
# 
#  
# Input:
# s = "acdcb"
# p = "a*c?b"
# Output: false
#  
#  Related Topics String Dynamic Programming Backtracking Greedy

def test():
    ts = [('a', '*', True), ('acdcb', 'a*c?b', False), ('adceb', '*a*b', True), ('cb', '?a', False), ('aa', '*', True),
          ('aa', 'a', False), ('', '*', True)]
    sol = Solution()
    for s, p, ans in ts:
        actual = sol.isMatch(s, p)
        print(s, p, ans, actual)
        if ans != actual:
            for i in range(len(s)):
                for j in range(len(p)):
                    print(s[i:], p[j:], match(s, i, p, j))
        assert ans == actual


# leetcode submit region begin(Prohibit modification and deletion)
from functools import lru_cache


@lru_cache(None)
def match(s, si, p, pi):
    if si == len(s) and pi == len(p):
        return True
    elif si < len(s) and pi == len(p):
        return False
    elif p[pi] == '*':
        while si <= len(s):
            if match(s, si, p, pi + 1):
                return True
            si += 1
        return False
    elif si == len(s) and pi < len(p):
        return False
    elif p[pi] == '?':
        return match(s, si + 1, p, pi + 1)
    elif s[si] == p[pi]:
        return match(s, si + 1, p, pi + 1)
    else:
        return False


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return match(s, 0, p, 0)
# leetcode submit region end(Prohibit modification and deletion)
