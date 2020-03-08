# Given a string s1, we may represent it as a binary tree by partitioning it to 
# two non-empty substrings recursively. 
# 
#  Below is one possible representation of s1 = "great": 
# 
#  
#     great
#    /    \
#   gr    eat
#  / \    /  \
# g   r  e   at
#            / \
#           a   t
#  
# 
#  To scramble the string, we may choose any non-leaf node and swap its two chil
# dren. 
# 
#  For example, if we choose the node "gr" and swap its two children, it produce
# s a scrambled string "rgeat". 
# 
#  
#     rgeat
#    /    \
#   rg    eat
#  / \    /  \
# r   g  e   at
#            / \
#           a   t
#  
# 
#  We say that "rgeat" is a scrambled string of "great". 
# 
#  Similarly, if we continue to swap the children of nodes "eat" and "at", it pr
# oduces a scrambled string "rgtae". 
# 
#  
#     rgtae
#    /    \
#   rg    tae
#  / \    /  \
# r   g  ta  e
#        / \
#       t   a
#  
# 
#  We say that "rgtae" is a scrambled string of "great". 
# 
#  Given two strings s1 and s2 of the same length, determine if s2 is a scramble
# d string of s1. 
# 
#  Example 1: 
# 
#  
# Input: s1 = "great", s2 = "rgeat"
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: s1 = "abcde", s2 = "caebd"
# Output: false 
#  Related Topics String Dynamic Programming

def test():
    ts = [('ab', 'ba', True), ('great', 'rgeat', True), ('abcde', 'caebd', False)]
    s = Solution()
    for a, b, ans in ts:
        actual = s.isScramble(a, b)
        print(a, b, ans, actual)
        assert ans == actual


# leetcode submit region begin(Prohibit modification and deletion)

from functools import lru_cache


@lru_cache(None)
def is_scramble(s1, s2):
    if set(s1) != set(s2):
        return False
    elif s1 == s2:
        return True
    n = len(s1)
    for i in range(1, len(s1)):
        if (is_scramble(s1[:i], s2[n - i:]) and is_scramble(s1[i:], s2[:n - i])) or (
                is_scramble(s1[:i], s2[:i]) and is_scramble(s1[i:], s2[i:])):
            return True
    return False


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        return is_scramble(s1, s2)
# leetcode submit region end(Prohibit modification and deletion)
