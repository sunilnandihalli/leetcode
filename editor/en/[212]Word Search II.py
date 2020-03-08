# Given a 2D board and a list of words from the dictionary, find all words in th
# e board. 
# 
#  Each word must be constructed from letters of sequentially adjacent cell, whe
# re "adjacent" cells are those horizontally or vertically neighboring. The same l
# etter cell may not be used more than once in a word. 
# 
#  
# 
#  Example: 
# 
#  
# Input: 
# board = [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
# words = ["oath","pea","eat","rain"]
# 
# Output: ["eat","oath"]
#  
# 
#  
# 
#  Note: 
# 
#  
#  All inputs are consist of lowercase letters a-z. 
#  The values of words are distinct. 
#  
#  Related Topics Backtracking Trie


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
# leetcode submit region end(Prohibit modification and deletion)
