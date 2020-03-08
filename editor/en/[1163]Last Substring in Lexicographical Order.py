# Given a string s, return the last substring of s in lexicographical order. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: "abab"
# Output: "bab"
# Explanation: The substrings are ["a", "ab", "aba", "abab", "b", "ba", "bab"]. 
# The lexicographically maximum substring is "bab".
#  
# 
#  Example 2: 
# 
#  
# Input: "leetcode"
# Output: "tcode"
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= s.length <= 4 * 10^5 
#  s contains only lowercase English letters. 
#  
#  Related Topics String Suffix Array
def test():
    ts = [('abab', 'bab'), ('leetcode', 'tcode')]
    sol = Solution()
    for s, ans in ts:
        actual = sol.lastSubstring(s)
        print(s, ans, actual)
        assert ans == actual


# leetcode submit region begin(Prohibit modification and deletion)
from functools import lru_cache


@lru_cache(None)
def gt(x, l, r):
    if l == len(x) and r == len(x):
        return True
    elif l < len(x) and r == len(x):
        return True
    elif l == len(x) and r < len(x):
        return False
    elif x[l] > x[r]:
        return True
    elif x[l] < x[r]:
        return False
    else:
        return gt(x, l + 1, r + 1)


def lss(x, s, e):
    if s + 1 < e:
        mid = (s + e) // 2
        l = lss(x, s, mid)
        r = lss(x, mid, e)
        return l if gt(x, l, r) else r
    else:
        return s

@lru_cache(None)
def max(x,i):

    maxi1 = max(x,i+1)

class Solution:
    def lastSubstring(self, s: str) -> str:
        for i in range(len(s) - 1, -1, -1):
            gt(s, i, i + 1)
        ans = lss(s, 0, len(s))
        return s[ans:]

# leetcode submit region end(Prohibit modification and deletion)
