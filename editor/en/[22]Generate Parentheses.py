# 
# Given n pairs of parentheses, write a function to generate all combinations of
#  well-formed parentheses.
#  
# 
#  
# For example, given n = 3, a solution set is:
#  
#  
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]
#  Related Topics String Backtracking
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
def gen(n):
    if n == 1:
        yield '()'
    else:
        for x in gen(n - 1):
            yield '()' + x
            yield '(' + x + ')'
            yield x+'()'

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return list(gen(n))
# leetcode submit region end(Prohibit modification and deletion)
