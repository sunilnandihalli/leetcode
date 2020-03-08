# Given an input string (s) and a pattern (p), implement regular expression matc
# hing with support for '.' and '*'. 
# 
#  
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
#  
# 
#  The matching should cover the entire input string (not partial). 
# 
#  Note: 
# 
#  
#  s could be empty and contains only lowercase letters a-z. 
#  p could be empty and contains only lowercase letters a-z, and characters like
#  . or *. 
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
# p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, 
# by repeating 'a' once, it becomes "aa".
#  
# 
#  Example 3: 
# 
#  
# Input:
# s = "ab"
# p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
#  
# 
#  Example 4: 
# 
#  
# Input:
# s = "aab"
# p = "c*a*b"
# Output: true
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, i
# t matches "aab".
#  
# 
#  Example 5: 
#

#  
# Input:
# s = "mississippi"
# p = "mis*is*p*."
# Output: false
#  
#  Related Topics String Dynamic Programming Backtracking


# leetcode submit region begin(Prohibit modification and deletion)
from functools import lru_cache


class Solution:
    @lru_cache(None)
    def cmatch(self, x):
        return (lambda c: True) if x == '.' else (lambda c: x == c)

    @lru_cache(None)
    def rmatch(self, si, pi):
        s = self.s
        if si == len(s) and pi == len(self.pattern_matcher):
            return True
        elif pi == len(self.pattern_matcher):
            return False
        pat = self.pattern_matcher[pi]
        if si == len(s) and len(pat) < 2:
            return False
        cmatch = self.cmatch(pat[0])
        if len(pat) == 2:
            if self.rmatch(si, pi + 1):
                return True
            while si < len(s) and cmatch(s[si]):
                if self.rmatch(si + 1, pi + 1):
                    return True
                si += 1
            return False
        else:
            return True if cmatch(s[si]) and self.rmatch(si + 1, pi + 1) else False

    def isMatch(self, s: str, p: str) -> bool:
        si = 0
        pi = 0
        pattern_matcher = []
        while pi < len(p):
            if pi + 1 < len(p) and p[pi + 1] == '*':
                pattern_matcher.append(p[pi:pi + 2])
                pi += 2
            else:
                pattern_matcher.append(p[pi])
                pi += 1
        print(pattern_matcher)
        self.pattern_matcher = pattern_matcher
        self.s = s
        return self.rmatch(0, 0)


# leetcode submit region end(Prohibit modification and deletion)
def test():
    ts = [("aa", "a", False),
          ('aa', 'a*', True),
          ('ab', '.*', True),
          ('aab', 'c*a*b*', True),
          ('mississippi', 'mis*is*p*.', False),
          ('a', 'ab*', True),
          ('ab', '.*c', False)]
    for s, p, ans in ts:
        sol = Solution()
        actual = sol.isMatch(s, p)
        print(s, p, ans, actual)
        assert ans == actual
