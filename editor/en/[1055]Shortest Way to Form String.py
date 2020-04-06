# From any string, we can form a subsequence of that string by deleting some num
# ber of characters (possibly no deletions). 
# 
#  Given two strings source and target, return the minimum number of subsequence
# s of source such that their concatenation equals target. If the task is impossib
# le, return -1. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: source = "abc", target = "abcbc"
# Output: 2
# Explanation: The target "abcbc" can be formed by "abc" and "bc", which are sub
# sequences of source "abc".
#  
# 
#  Example 2: 
# 
#  
# Input: source = "abc", target = "acdbc"
# Output: -1
# Explanation: The target string cannot be constructed from the subsequences of 
# source string due to the character "d" in target string.
#  
# 
#  Example 3: 
# 
#  
# Input: source = "xyz", target = "xzyxz"
# Output: 3
# Explanation: The target string can be constructed as follows "xz" + "y" + "xz"
# .
#  
#  
#  Constraints: 
# 
#  
#  Both the source and target strings consist of only lowercase English letters 
# from "a"-"z". 
#  The lengths of source and target string are between 1 and 1000. 
#  Related Topics Dynamic Programming Greedy

def test():
    ts = [('abc', 'abcbc', 2), ('abc', 'acdbc', -1), ('xyz', 'xzyxz', 3)]
    for a, b, ans in ts:
        s = Solution()
        actual = s.shortestWay(a, b)
        print(a, b, ans, actual)
        assert ans == actual


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        i = 0
        num_substrs = 0
        while i < len(target):
            progress = False
            for x in source:
                if x == target[i]:
                    progress = True
                    i += 1
                    if i == len(target):
                        break
            if progress:
                num_substrs += 1
            else:
                return -1
        return num_substrs
# leetcode submit region end(Prohibit modification and deletion)
