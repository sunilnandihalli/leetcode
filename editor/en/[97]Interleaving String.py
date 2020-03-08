# Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2. 
# 
# 
#  Example 1: 
# 
#  
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false
#  
#  Related Topics String Dynamic Programming


# leetcode submit region begin(Prohibit modification and deletion)

from functools import lru_cache


def test():
    ts = [("aabcc", "dbbca", "aadbbcbcac", True), ("aabcc", "dbbca", "aadbbbaccc", False)]
    s = Solution()
    for s1, s2, s3, ans in ts:
        actual = s.isInterleave(s1, s2, s3)
        print(s1, s2, s3, ans, actual)
        assert ans == actual


@lru_cache(None)
def is_interleave(s1, s2, s3, i, j):
    if i + j == len(s3):
        return True
    elif i < len(s1) and s1[i] == s3[i + j] and is_interleave(s1, s2, s3, i + 1, j):
        return True
    elif j < len(s2) and s2[j] == s3[i + j] and is_interleave(s1, s2, s3, i, j + 1):
        return True
    else:
        return False


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        else:
            for i in range(len(s1) - 1, -1, -1):
                for j in range(len(s2) - 1, -1, -1):
                    is_interleave(s1, s2, s3, i, j)
            return is_interleave(s1, s2, s3, 0, 0)

# leetcode submit region end(Prohibit modification and deletion)
