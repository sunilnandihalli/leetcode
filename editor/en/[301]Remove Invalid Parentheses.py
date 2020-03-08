# Remove the minimum number of invalid parentheses in order to make the input st
# ring valid. Return all possible results. 
# 
#  Note: The input string may contain letters other than the parentheses ( and )
# . 
# 
#  Example 1: 
# 
#  
# Input: "()())()"
# Output: ["()()()", "(())()"]
#  
# 
#  Example 2: 
# 
#  
# Input: "(a)())()"
# Output: ["(a)()()", "(a())()"]
#  
# 
#  Example 3: 
# 
#  
# Input: ")("
# Output: [""]
#  Related Topics Depth-first Search Breadth-first Search
from more_itertools import

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:

    # leetcode submit region end(Prohibit modification and deletion)


def test():
    ts = [("()())()", ["()()()", "(())()"]), ("(a)())()", ["(a)()()", "(a())()"]), (")(", [""])]
    s = Solution()
    for x, ans in ts:
        actual = s.removeInvalidParentheses(x)
        assert sorted(actual) == sorted(ans)
