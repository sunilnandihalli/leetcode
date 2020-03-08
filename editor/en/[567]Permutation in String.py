# Given two strings s1 and s2, write a function to return true if s2 contains th
# e permutation of s1. In other words, one of the first string's permutations is t
# he substring of the second string. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: s1 = "ab" s2 = "eidbaooo"
# Output: True
# Explanation: s2 contains one permutation of s1 ("ba").
#  
# 
#  Example 2: 
# 
#  
# Input:s1= "ab" s2 = "eidboaoo"
# Output: False
#  
# 
#  
# 
#  Note: 
# 
#  
#  The input strings only contain lower case letters. 
#  The length of both given strings is in range [1, 10,000]. 
#  
#  Related Topics Two Pointers Sliding Window


# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        x = Counter(s1)
        for c in s2:
            if c in x:
                x[c] -= 1
                if x[c] == 0:
                    del x[c]
            else:
                x = Counter(s1)
            if len(x) == 0:
                return True

# leetcode submit region end(Prohibit modification and deletion)
