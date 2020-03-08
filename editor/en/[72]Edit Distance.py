# Given two words word1 and word2, find the minimum number of operations require
# d to convert word1 to word2. 
# 
#  You have the following 3 operations permitted on a word: 
# 
#  
#  Insert a character 
#  Delete a character 
#  Replace a character 
#  
# 
#  Example 1: 
# 
#  
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
#  
# 
#  Example 2: 
# 
#  
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation: 
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')
#  
#  Related Topics String Dynamic Programming
def test():
    ts = [('horse', 'ros', 3), ('intention', 'execution', 5)]
    s = Solution()
    for w1, w2, ans in ts:
        actual = s.minDistance(w1, w2)
        print(w1, w2, ans, actual)
        assert actual == ans


# leetcode submit region begin(Prohibit modification and deletion)
from functools import lru_cache


@lru_cache(None)
def mdist(w1, w2):
    if w1 == w2:
        return 0
    else:
        ret = float('inf')
        # replace
        for i, x in enumerate(w1):
            for j, y in enumerate(w2):
                ret = min(ret, mdist(w1[:i] + y + w1[i + 1:], w2))

        # remove
        for i, x in enumerate(w1):
            ret = min(ret, mdist(w1[:i] + w1[i + 1:], w2))

        # insert
        for i in range(len(w1)):
            for x in w2:
                ret = min(ret, mdist(w1[:i] + x + w1[i:], w2))
        return ret


@lru_cache(None)
def mdists(w1, w2):
    if w1 == w2:
        return 0
    elif len(w1) > 0 and len(w2) > 0:
        if w1[-1] == w2[-1]:
            return mdists(w1[:-1], w2[:-1])
        else:
            # replace
            v1 = mdists(w1[:-1], w2[:-1]) + 1

            # insert
            v2 = mdists(w1, w2[:-1]) + 1

            # remove
            v3 = mdists(w1[:-1], w2) + 1
            return min([v1, v2, v3])
    else:
        return max(len(w1), len(w2))


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        return mdists(word1, word2)

# leetcode submit region end(Prohibit modification and deletion)
