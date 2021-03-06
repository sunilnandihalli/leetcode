# Given a non-empty string s and a dictionary wordDict containing a list of non-
# empty words, add spaces in s to construct a sentence where each word is a valid 
# dictionary word. Return all such possible sentences. 
# 
#  Note: 
# 
#  
#  The same word in the dictionary may be reused multiple times in the segmentat
# ion. 
#  You may assume the dictionary does not contain duplicate words. 
#  
# 
#  Example 1: 
# 
#  
# Input:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# Output:a
# [
#   "cats and dog",
#   "cat sand dog"
# ]
#  
# 
#  Example 2: 
# 
#  
# Input:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# Output:
# [
#   "pine apple pen apple",
#   "pineapple pen apple",
#   "pine applepen apple"
# ]
# Explanation: Note that you are allowed to reuse a dictionary word.
#  
# 
#  Example 3: 
# 
#  
# Input:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output:
# [] 
#  Related Topics Dynamic Programming Backtracking


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
# leetcode submit region end(Prohibit modification and deletion)
