# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
#  determine if the input string is valid. 
# 
#  An input string is valid if: 
# 
#  
#  Open brackets must be closed by the same type of brackets. 
#  Open brackets must be closed in the correct order. 
#  
# 
#  Note that an empty string is also considered valid. 
# 
#  Example 1: 
# 
#  
# Input: "()"
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: "()[]{}"
# Output: true
#  
# 
#  Example 3: 
# 
#  
# Input: "(]"
# Output: false
#  
# 
#  Example 4: 
# 
#  
# Input: "([)]"
# Output: false
#  
# 
#  Example 5: 
# 
#  
# Input: "{[]}"
# Output: true
#  
#  Related Topics String Stack


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        open_brackets = set('{[(')
        close_brackets = set('}])')
        close_brakcet_map = {a: b for a, b in zip('{[(', '}])')}
        for x in s:
            if x in open_brackets:
                stk.append(x)
            elif x in close_brackets:
                if len(stk) == 0 or x != close_brakcet_map[stk.pop()]:
                    return False
        return len(stk) == 0
# leetcode submit region end(Prohibit modification and deletion)
