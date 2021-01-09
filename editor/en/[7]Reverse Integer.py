# Given a 32-bit signed integer, reverse digits of an integer. 
# 
#  Example 1: 
# 
#  
# Input: 123
# Output: 321
#  
# 
#  Example 2: 
# 
#  
# Input: -123
# Output: -321
#  
# 
#  Example 3: 
# 
#  
# Input: 120
# Output: 21
#  
# 
#  Note: 
# Assume we are dealing with an environment which could only store integers with
# in the 32-bit signed integer range: [−231, 231 − 1]. For the purpose of this pro
# blem, assume that your function returns 0 when the reversed integer overflows. 
#  Related Topics Math


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverse(self, x: int) -> int:
        max_int = 2 ** 31 - 1
        min_int = -max_int - 1
        if x < min_int or x > max_int:
            return 0
        if x < 0:
            neg = True
            x = -x
        else:
            neg = False

        ret = 0
        while x > 0:
            x, d = divmod(x, 10)
            ret = ret * 10 + d
        ret *= (-1 if neg else 1)
        return 0 if ret < min_int or ret > max_int else ret

# leetcode submit region end(Prohibit modification and deletion)
