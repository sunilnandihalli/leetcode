# Given a string, find the length of the longest substring T that contains at mo
# st k distinct characters. 
# 
#  Example 1: 
# 
#  
#  
# Input: s = "eceba", k = 2
# Output: 3
# Explanation: T is "ece" which its length is 3. 
# 
#  
#  Example 2: 
# 
#  
# Input: s = "aa", k = 1
# Output: 2
# Explanation: T is "aa" which its length is 2.
#  
#  
#  Related Topics Hash Table String Sliding Window


# leetcode submit region begin(Prohibit modification and deletion)

class Solution:

    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:

# leetcode submit region end(Prohibit modification and deletion)
def test():
    ts = [('aa',1,2),('eceba',2,3)]
    sol = Solution()
    for s,k,ans in ts:
        actual = sol.lengthOfLongestSubstringKDistinct(s,k)
        print(s,k,ans,actual)
        assert(actual==ans)