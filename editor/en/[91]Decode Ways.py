# A message containing letters from A-Z is being encoded to numbers using the fo
# llowing mapping: 
# 
#  
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
#  
# 
#  Given a non-empty string containing only digits, determine the total number o
# f ways to decode it. 
# 
#  Example 1: 
# 
#  
# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
#  
# 
#  Example 2: 
# 
#  
# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6)
# . 
#  Related Topics String Dynamic Programming

def test():
    ts = [('12', 2), ('226', 3)]
    sol = Solution()
    for s, ans in ts:
        actual = sol.numDecodings(s)
        print(s, ans, actual)
        assert ans == actual


# leetcode submit region begin(Prohibit modification and deletion)


from functools import lru_cache

code = {str(i + 1): chr(i + ord('A')) for i in range(26)}


@lru_cache(None)
def num_decodings(s, i):
    if i == len(s):
        return 1
    ret = 0
    if s[i] in code:
        ret += num_decodings(s, i + 1)
    if i < len(s) - 1 and s[i:i + 2] in code:
        ret += num_decodings(s, i + 2)
    return ret


class Solution:
    def numDecodings(self, s: str) -> int:
        for i in range(len(s) - 1, -1, -1):
            num_decodings(s, i)
        return num_decodings(s, 0)
# leetcode submit region end(Prohibit modification and deletion)
