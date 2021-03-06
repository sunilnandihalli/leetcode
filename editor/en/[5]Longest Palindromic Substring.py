# Given a string s, find the longest palindromic substring in s. You may assume 
# that the maximum length of s is 1000. 
# 
#  Example 1: 
# 
#  
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
#  
# 
#  Example 2: 
# 
#  
# Input: "cbbd"
# Output: "bb"
#  
#  Related Topics String Dynamic Programming


# leetcode submit region begin(Prohibit modification and deletion)
from functools import lru_cache


@lru_cache(None)
def lp(s, i, j):  # inclusive of the end-points
    if i > j:
        return ''
    elif i == j:
        return s[i]
    if s[i] == s[j]:
        return s[i] + lp(s, i + 1, j - 1) + s[j]
    else:
        a = lp(s, i, j - 1)
        b = lp(s, i + 1, j)
        return a if len(a) >= len(b) else b


@lru_cache(None)
def ispa(s, i, j):  # inclusive of the end-points
    if i == j:
        return True
    elif i + 1 == j:
        return s[i] == s[j]
    else:
        if s[i] == s[j]:
            return ispa(s, i + 1, j - 1)
        else:
            return False


def max_pa(s):
    mi = 0
    mj = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if ispa(s, i, j):
                if j - i + 1 > mj - mi + 1:
                    mi = i
                    mj = j
    return s[mi:mj + 1]


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # return lp(s, 0, len(s) - 1)
        return max_pa(s)

    # leetcode submit region end(Prohibit modification and deletion)


def test():
    ts = [('bb', 'bb')]
    for inp, ans in ts:
        actual = max_pa(inp)
        print(inp, actual, ans)
        assert actual == ans
