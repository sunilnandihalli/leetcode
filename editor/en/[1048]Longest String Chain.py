# Given a list of words, each word consists of English lowercase letters. 
# 
#  Let's say word1 is a predecessor of word2 if and only if we can add exactly o
# ne letter anywhere in word1 to make it equal to word2. For example, "abc" is a p
# redecessor of "abac". 
# 
#  A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1
# , where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, an
# d so on. 
# 
#  Return the longest possible length of a word chain with words chosen from the
#  given list of words. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: ["a","b","ba","bca","bda","bdca"]
# Output: 4
# Explanation: one of the longest word chain is "a","ba","bda","bdca".
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= words.length <= 1000 
#  1 <= words[i].length <= 16 
#  words[i] only consists of English lowercase letters. 
#  
# 
#  
#  
#  Related Topics Hash Table Dynamic Programming

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)

from functools import lru_cache


class Solution:
    @lru_cache(None)
    def chain_length(self, w):
        if len(w) == 1:
            return 1
        ret = 1
        for i in range(len(w)):
            x = w[:i] + w[i + 1:]
            if x in self.words:
                ret = max(1 + self.chain_length(x), ret)
        return ret

    def longestStrChain(self, words: List[str]) -> int:
        self.words = set(words)
        return max([self.chain_length(w) for w in words])

# leetcode submit region end(Prohibit modification and deletion)
