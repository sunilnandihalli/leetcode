# Given a string s , find the length of the longest substring t that contains at
#  most 2 distinct characters. 
# 
#  Example 1: 
# 
#  
# Input: "eceba"
# Output: 3
# Explanation: t is "ece" which its length is 3.
#  
# 
#  Example 2: 
# 
#  
# Input: "ccaabbb"
# Output: 5
# Explanation: t is "aabbb" which its length is 5.
#  
#  Related Topics Hash Table Two Pointers String Sliding Window


# leetcode submit region begin(Prohibit modification and deletion)
def remove(cur_alphabets, chr):
    assert chr in cur_alphabets
    cur_alphabets[chr] -= 1
    if cur_alphabets[chr] == 0:
        cur_alphabets.pop(chr)

from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        i = 0
        j = 0
        cur_alphabets = defaultdict(int)
        ans = 0
        ans_i = 0
        ans_j = 0
        while i<len(s) and j<len(s):
            while j < len(s):
                if len(cur_alphabets) == 2 and s[j] not in cur_alphabets:
                    break
                cur_alphabets[s[j]] += 1
                j += 1

            if ans < j - i:
                ans = j - i
                ans_i = i
                ans_j = j

            while i < len(s):
                if len(cur_alphabets) < 2:
                    break
                remove(cur_alphabets, s[i])
                i += 1
        return ans
# leetcode submit region end(Prohibit modification and deletion)
