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

def kmp_test():
    ts = [('abcxabcxyzabc', [0, 0, 0, 0, 1, 2, 3, 4, 0, 0, 1, 2, 3])]
    for p, p_kmp in ts:
        actual = kmp(p)
        print(p, p_kmp, actual)
        assert p_kmp == actual


def test():
    ts = [('abcdebdde', 'bde', 'bcde'), ('', 'abcd', ''), ('abcde', '', ''), ('abbde', 'bde', 'bde'),
          ('abcbcde', 'bde', 'bcde')]
    for s, t, ans in ts:
        sol = Solution()
        actual = sol.minWindow(s, t)
        print(s, t, ans, actual)
        assert ans == actual


# leetcode submit region begin(Prohibit modification and deletion)

@lru_cache(None)
def kmp(p):
    x = [0]
    j = 0
    i = 1
    while i < len(p):
        j = j + 1 if p[i] == p[j] else x[j - 1] if j > 0 else 0
        x.append(j)
        i += 1
    return tuple(x)


from functools import lru_cache


@lru_cache(None)
def match(s, p, i, j):  # length of the pattern matched by some subsequence of s[i:j]
    if i == j:
        return 0
    else:
        pmatch = match(s, p, i, j - 1)
        if p[pmatch] == s[j - 1]:
            return pmatch + 1
        else:
            return pmatch


def full_match(s, p, i):
    j = i + len(p)
    while match(s, p, i, j) < len(p):
        j += 1
    return j

def smallest_window(s,p,i): # smallest window containing the string starting from
    pass

class Solution:
    def minWindow(self, S: str, T: str) -> str:

# leetcode submit region end(Prohibit modification and deletion)
