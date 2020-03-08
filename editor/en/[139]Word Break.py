# Given a non-empty string s and a dictionary wordDict containing a list of non-
# empty words, determine if s can be segmented into a space-separated sequence of 
# one or more dictionary words. 
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
# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
#  
# 
#  Example 2: 
# 
#  
# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pe
# n apple".
#              Note that you are allowed to reuse a dictionary word.
#  
# 
#  Example 3: 
# 
#  
# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false
#  
#  Related Topics Dynamic Programming


# leetcode submit region begin(Prohibit modification and deletion)
def rolling_hash(w, p, k):
    ret = 0
    prod = 1
    for x in w:
        ret = (ret + ord(x) * prod) % k
        prod = (prod * p) % k
    return ret


from functools import lru_cache
from collections import defaultdict
@lru_cache(None)
def break_word(x,wdict,s,e):
    dictionary_hashes = defaultdict(set)
    for x in wdict:
        hx = rolling_hash(x)
        dictionary_hashes[hx].add(x)

    rhash = 0


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:


# leetcode submit region end(Prohibit modification and deletion)
def test():
    ts = [("leetcode", ["leet", "code"], True),
          ("applepenapple", ["apple", "pen"], True),
          ("catsandog", ["cats", "dog", "sand", "and", "cat"], False)]
    sol = Solution()
    for s, word_dict, ans in ts:
        actual = sol.wordBreak(s, word_dict)
        print(s, word_dict, ans, actual)
        assert ans == actual
