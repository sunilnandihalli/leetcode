# Given an array of words and a width maxWidth, format the text such that each l
# ine has exactly maxWidth characters and is fully (left and right) justified. 
# 
#  You should pack your words in a greedy approach; that is, pack as many words 
# as you can in each line. Pad extra spaces ' ' when necessary so that each line h
# as exactly maxWidth characters. 
# 
#  Extra spaces between words should be distributed as evenly as possible. If th
# e number of spaces on a line do not divide evenly between words, the empty slots
#  on the left will be assigned more spaces than the slots on the right. 
# 
#  For the last line of text, it should be left justified and no extra space is 
# inserted between words. 
# 
#  Note: 
# 
#  
#  A word is defined as a character sequence consisting of non-space characters 
# only. 
#  Each word's length is guaranteed to be greater than 0 and not exceed maxWidth
# . 
#  The input array words contains at least one word. 
#  
# 
#  Example 1: 
# 
#  
# Input:
# words = ["This", "is", "an", "example", "of", "text", "justification."]
# maxWidth = 16
# Output:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
#  
# 
#  Example 2: 
# 
#  
# Input:
# words = ["What","must","be","acknowledgment","shall","be"]
# maxWidth = 16
# Output:
# [
#   "What   must   be",
#   "acknowledgment  ",
#   "shall be        "
# ]
# Explanation: Note that the last line is "shall be    " instead of "shall     b
# e",
#              because the last line must be left-justified instead of fully-jus
# tified.
#              Note that the second line is also left-justified becase it contai
# ns only one word.
#  
# 
#  Example 3: 
# 
#  
# Input:
# words = ["Science","is","what","we","understand","well","enough","to","explain
# ",
#          "to","a","computer.","Art","is","everything","else","we","do"]
# maxWidth = 20
# Output:
# [
#   "Science  is  what we",
#   "understand      well",
#   "enough to explain to",
#   "a  computer.  Art is",
#   "everything  else  we",
#   "do                  "
# ]
#  
#  Related Topics String
from typing import List


def test():
    ts = [(["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.",
            "Art", "is", "everything", "else", "we", "do"], 20,
           ["Science  is  what we",
            "understand      well",
            "enough to explain to",
            "a  computer.  Art is",
            "everything  else  we",
            "do                  "]),
          (["What", "must", "be", "acknowledgment", "shall", "be"], 16, '')][1:]
    for x, w, ans in ts:
        s = Solution()
        actual = s.fullJustify(x, w)
        print('\n'.join(actual))
        assert actual == ans


# leetcode submit region begin(Prohibit modification and deletion)


def justify(words, maxwidth):
    wls = [len(s) for s in words]
    cwls = [0]
    for x in wls:
        cwls.append(x + cwls[-1])
    line_len = lambda i, j: (cwls[j + 1] - cwls[i]) + (j - i)
    line_start = 0
    ret = []
    while line_start < len(words):
        line_end = line_start
        while line_end + 1 < len(words) and line_len(line_start, line_end + 1) <= maxwidth:
            line_end += 1
        extra_gap = maxwidth - line_len(line_start, line_end)
        if line_end < len(words) - 1:
            num_interleaving_spaces = line_end - line_start
            if num_interleaving_spaces > 0:
                equal_increase, extra_increase = divmod(extra_gap, num_interleaving_spaces)
                ret.append(' '.join([x + ' ' * (equal_increase + (1 if i < extra_increase else 0)) for i, x in
                                     enumerate(words[line_start:line_end])]) + ' ' + words[line_end])
        else:
            ret.append(' '.join(words[line_start:line_end + 1]) + ' ' * extra_gap)
        line_start = line_end + 1
    return ret


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        return justify(words, maxWidth)
# leetcode submit region end(Prohibit modification and deletion)
