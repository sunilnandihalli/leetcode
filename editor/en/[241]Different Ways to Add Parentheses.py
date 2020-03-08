# Given a string of numbers and operators, return all possible results from comp
# uting all the different possible ways to group numbers and operators. The valid 
# operators are +, - and *. 
# 
#  Example 1: 
# 
#  
# Input: "2-1-1"
# Output: [0, 2]
# Explanation: 
# ((2-1)-1) = 0 
# (2-(1-1)) = 2 
# 
#  Example 2: 
# 
#  
# Input: "2*3-4*5"
# Output: [-34, -14, -10, -10, 10]
# Explanation: 
# (2*(3-(4*5))) = -34 
# ((2*3)-(4*5)) = -14 
# ((2*(3-4))*5) = -10 
# (2*((3-4)*5)) = -10 
# (((2*3)-4)*5) = 10
#  Related Topics Divide and Conquer
from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
ops = {'*': lambda x, y: x * y,
       '+': lambda x, y: x + y,
       '-': lambda x, y: x - y}


def parse_input(s):
    i = 0
    l = []
    while i < len(s):
        j = i
        while j < len(s) and s[j] not in ops:
            j += 1
        l.append(int(s[i:j]))
        if j < len(s):
            l.append(ops[s[j]])
            j += 1
        i = j
    return l


from itertools import chain


def compute(l):
    if len(l) == 1:
        return l
    else:
        ret = []
        for fid in range(1, len(l), 2):
            for x in compute(l[:fid]):
                for y in compute(l[fid + 1:]):
                    ret.append(l[fid](x, y))
        return ret


class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        return compute(parse_input(input))

# leetcode submit region end(Prohibit modification and deletion)
