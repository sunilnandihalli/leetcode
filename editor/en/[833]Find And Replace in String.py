# To some string S, we will perform some replacement operations that replace gro
# ups of letters with new ones (not necessarily the same size). 
# 
#  Each replacement operation has 3 parameters: a starting index i, a source wor
# d x and a target word y. The rule is that if x starts at position i in the origi
# nal string S, then we will replace that occurrence of x with y. If not, we do no
# thing. 
# 
#  For example, if we have S = "abcd" and we have some replacement operation i =
#  2, x = "cd", y = "ffff", then because "cd" starts at position 2 in the original
#  string S, we will replace it with "ffff". 
# 
#  Using another example on S = "abcd", if we have both the replacement operatio
# n i = 0, x = "ab", y = "eee", as well as another replacement operation i = 2, x 
# = "ec", y = "ffff", this second operation does nothing because in the original s
# tring S[2] = 'c', which doesn't match x[0] = 'e'. 
# 
#  All these operations occur simultaneously. It's guaranteed that there won't b
# e any overlap in replacement: for example, S = "abc", indexes = [0, 1], sources 
# = ["ab","bc"] is not a valid test case. 
# 
#  Example 1: 
# 
#  
# Input: S = "abcd", indexes = [0,2], sources = ["a","cd"], targets = ["eee","ff
# ff"]
# Output: "eeebffff"
# Explanation: "a" starts at index 0 in S, so it's replaced by "eee".
# "cd" starts at index 2 in S, so it's replaced by "ffff".
#  
# 
#  Example 2: 
# 
#  
# Input: S = "abcd", indexes = [0,2], sources = ["ab","ec"], targets = ["eee","f
# fff"]
# Output: "eeecd"
# Explanation: "ab" starts at index 0 in S, so it's replaced by "eee". 
# "ec" doesn't starts at index 2 in the original S, so we do nothing.
#  
# 
#  Notes: 
# 
#  
#  0 <= indexes.length = sources.length = targets.length <= 100 
#  0 < indexes[i] < S.length <= 1000 
#  All characters in given inputs are lowercase letters. 
#  
# 
#  
#  Related Topics String


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        
# leetcode submit region end(Prohibit modification and deletion)
