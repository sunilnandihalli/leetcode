# Roman numerals are represented by seven different symbols: I, V, X, L, C, D an
# d M. 
# 
#  
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000 
# 
#  For example, two is written as II in Roman numeral, just two one's added toge
# ther. Twelve is written as, XII, which is simply X + II. The number twenty seven
#  is written as XXVII, which is XX + V + II. 
# 
#  Roman numerals are usually written largest to smallest from left to right. Ho
# wever, the numeral for four is not IIII. Instead, the number four is written as 
# IV. Because the one is before the five we subtract it making four. The same prin
# ciple applies to the number nine, which is written as IX. There are six instance
# s where subtraction is used: 
# 
#  
#  I can be placed before V (5) and X (10) to make 4 and 9. 
#  X can be placed before L (50) and C (100) to make 40 and 90. 
#  C can be placed before D (500) and M (1000) to make 400 and 900. 
#  
# 
#  Given a roman numeral, convert it to an integer. Input is guaranteed to be wi
# thin the range from 1 to 3999. 
# 
#  Example 1: 
# 
#  
# Input: "III"
# Output: 3 
# 
#  Example 2: 
# 
#  
# Input: "IV"
# Output: 4 
# 
#  Example 3: 
# 
#  
# Input: "IX"
# Output: 9 
# 
#  Example 4: 
# 
#  
# Input: "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
#  
# 
#  Example 5: 
# 
#  
# Input: "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4. 
#  Related Topics Math String


# leetcode submit region begin(Prohibit modification and deletion)


def split_when(arr, pred):
    ret = []

    i = 0
    while i < len(arr):
        cg = [arr[i]]
        i += 1
        while i < len(arr) and not pred(arr[i - 1], arr[i]):
            cg.append(arr[i])
            i += 1
        ret.append(cg)
    return ret


v = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


class Solution:
    def romanToInt(self, s: str) -> int:
        terms = split_when(s, lambda x, y: v[x] > v[y])
        ret = 0
        for t in terms:
            vals = [v[x] for x in t]
            if max(vals) == min(vals):
                ret += sum(vals)
            else:
                s = v[t[-1]]
                for i in range(len(t) - 1):
                    s -= v[t[i]]
                ret += s
        return ret


# leetcode submit region end(Prohibit modification and deletion)

def test():
    ts = [('MCMXCIV', 1994), ('LVIII', 58), ('I', 1), ('CD', 400), ('CMIC', 999)]
    sol = Solution()
    for r, ans in ts:
        actual = sol.romanToInt(r)
        print(r, ans, actual)
        assert ans == actual
