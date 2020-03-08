# Given a string s of '(' , ')' and lowercase English characters. 
# 
#  Your task is to remove the minimum number of parentheses ( '(' or ')', in any
#  positions ) so that the resulting parentheses string is valid and return any va
# lid string. 
# 
#  Formally, a parentheses string is valid if and only if: 
# 
#  
#  It is the empty string, contains only lowercase characters, or 
#  It can be written as AB (A concatenated with B), where A and B are valid stri
# ngs, or 
#  It can be written as (A), where A is a valid string. 
#  
# 
#  
#  Example 1: lee(t(c)o)de
# 
#  
# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "a)b(c)d"
# Output: "ab(c)d"
#  
# 
#  Example 3: 
# 
#  
# Input: s = "))(("
# Output: ""
# Explanation: An empty string is also valid.
#  
# 
#  Example 4: 
# 
#  
# Input: s = "(a(b(c)d)"
# Output: "a(b(c)d)"
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10^5 
#  s[i] is one of '(' , ')' and lowercase English letters. 
#  Related Topics String Stack


# leetcode submit region begin(Prohibit modification and deletion)
open_bracket = '('
close = ')'
parens = set([open_bracket, close])


def is_valid(s):
    stk = []
    for c in s:
        if c == open_bracket:
            stk.append(c)
        elif c == close:
            if len(stk) == 0:
                return False
            stk.pop()
    return len(stk) == 0


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ret = ''
        num_open_brackets = 0
        for x in s:
            if x == open_bracket:
                num_open_brackets += 1
                ret += x
            elif x == close:
                if num_open_brackets > 0:
                    num_open_brackets -= 1
                    ret += x
            else:
                ret += x
        num_close_brackets = 0
        bret = ''
        for x in reversed(ret):
            if x == close:
                num_close_brackets += 1
                bret = x + bret
            elif x == open_bracket:
                if num_close_brackets > 0:
                    num_close_brackets -= 1
                    bret = x + bret
            else:
                bret = x + bret
        return bret


# leetcode submit region end(Prohibit modification and deletion)

def test():
    ts = [('lee(t(c)o)de)', 'lee(t(c)o)de'),
          ('a)b(c)d', 'ab(c)d'),
          ('))((', ''),
          ('(a(b(c)d)', 'a(b(c)d)')]
    s = Solution()
    for x, ans in ts:
        actual = s.minRemoveToMakeValid(x)
        print(x, ans, actual)
        assert ans == actual
