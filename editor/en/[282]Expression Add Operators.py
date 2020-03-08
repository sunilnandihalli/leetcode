# Given a string that contains only digits 0-9 and a target value, return all po
# ssibilities to add binary operators (not unary) +, -, or * between the digits so
#  they evaluate to the target value. 
# 
#  Example 1: 
# 
#  
# Input: num = "123", target = 6
# Output: ["1+2+3", "1*2*3"] 
#  
# 
#  Example 2: 
# 
#  
# Input: num = "232", target = 8
# Output: ["2*3+2", "2+3*2"] 
# 
#  Example 3: 
# 
#  
# Input: num = "105", target = 5
# Output: ["1*0+5","10-5"] 
# 
#  Example 4: 
# 
#  
# Input: num = "00", target = 0
# Output: ["0+0", "0-0", "0*0"]
#  
# 
#  Example 5: 
# 
#  
# Input: num = "3456237490", target = 9191
# Output: []
#  
#  Related Topics Divide and Conquer
from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        pass


# leetcode submit region end(Prohibit modification and deletion)
def test():
    ts = [('123', 6, ['1+2+3', '1*2*3']),
          ('232', 8, ['2*3+2', '2+3*2']),
          ('105', 5, ['1*0+5', '10-5']),
          ('00', 0, ['0+0', '0-0', '0*0'])]
