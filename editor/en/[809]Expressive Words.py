# Sometimes people repeat letters to represent extra feeling, such as "hello" ->
#  "heeellooo", "hi" -> "hiiii". In these strings like "heeellooo", we have groups
#  of adjacent letters that are all the same: "h", "eee", "ll", "ooo". 
# 
#  For some given string S, a query word is stretchy if it can be made to be equ
# al to S by any number of applications of the following extension operation: choo
# se a group consisting of characters c, and add some number of characters c to th
# e group so that the size of the group is 3 or more. 
# 
#  For example, starting with "hello", we could do an extension on the group "o"
#  to get "hellooo", but we cannot get "helloo" since the group "oo" has size less
#  than 3. Also, we could do another extension like "ll" -> "lllll" to get "hellll
# looo". If S = "helllllooo", then the query word "hello" would be stretchy becaus
# e of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo
# " = S. 
# 
#  Given a list of query words, return the number of words that are stretchy. 
# 
#  
# 
#  
# Example:
# Input: 
# S = "heeellooo"
# words = ["hello", "hi", "helo"]
# Output: 1
# Explanation: 
# We can extend "e" and "o" in the word "hello" to get "heeellooo".
# We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3
#  or more.
#  
# 
#  
# 
#  Notes: 
# 
#  
#  0 <= len(S) <= 100. 
#  0 <= len(words) <= 100. 
#  0 <= len(words[i]) <= 100. 
#  S and all words in words consist only of lowercase letters 
#  
# 
#  
#  Related Topics String
from typing import List


def test():
    ts = [('aaa', ['aaaa'], 0),
          ('dddinso', ['ddinso'], 1),
          ('heeellooo', ['hello', 'hi', 'helo'], 1),
          ('helllllooo', ['helo', 'hi', 'hello'], 2),
          ("dddiiiinnssssssoooo",
           ["dinnssoo", "ddinso",
            "ddiinnso",
            "ddiinnssoo",
            "ddiinso", "dinsoo",
            "ddiinsso",
            "dinssoo", "dinso"],
           3)]
    for s, words, ans in ts:
        sol = Solution()
        actual = sol.expressiveWords(s, words)
        print(s, words, ans, actual)
        assert ans == actual


# leetcode submit region begin(Prohibit modification and deletion)
def is_extension_of(s, word, i, j):
    if i == len(s) and j == len(word):
        return True
    elif i == len(s) or j == len(word):
        return False
    dj = j
    while dj < len(word) and word[dj] == word[j]:
        dj += 1
    c = i
    while c < len(s) and s[c] == word[j]:
        c += 1
        if ((c - i >= 3 and c - i > dj - j) or c - i == dj - j) and is_extension_of(s, word, c, dj):
            return True
    return False


class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        ret = 0
        for word in words:
            if is_extension_of(S, word, 0, 0):
                ret += 1
        return ret
# leetcode submit region end(Prohibit modification and deletion)
