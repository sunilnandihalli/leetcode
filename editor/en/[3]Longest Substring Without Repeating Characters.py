# Given a string, find the length of the longest substring without repeating cha
# racters. 
# 
#  
#  Example 1: 
# 
#  
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
#  
# 
#  
#  Example 2: 
# 
#  
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#  
# 
#  
#  Example 3: 
# 
#  
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
#              Note that the answer must be a substring, "pwke" is a subsequence
#  and not a substring.
#  
#  
#  
#  
#  Related Topics Hash Table Two Pointers String Sliding Window


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        cur_alphabets = set()
        ans = 0
        ans_i = 0
        ans_j = 0
        while i < len(s) and j < len(s):
            while j < len(s) and s[j] not in cur_alphabets:
                cur_alphabets.add(s[j])
                j += 1
            if j - i > ans:
                ans = j-i
                ans_i = i
                ans_j = j
            while i < len(s) and j < len(s) and s[i] != s[j]:
                cur_alphabets.remove(s[i])
                i += 1
            cur_alphabets.remove(s[i])
            i += 1
        return ans

# leetcode submit region end(Prohibit modification and deletion)
