# Given a non-empty string check if it can be constructed by taking a substring 
# of it and appending multiple copies of the substring together. You may assume th
# e given string consists of lowercase English letters only and its length will no
# t exceed 10000. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: "abab"
# Output: True
# Explanation: It's the substring "ab" twice.
#  
# 
#  Example 2: 
# 
#  
# Input: "aba"
# Output: False
#  
# 
#  Example 3: 
# 
#  
# Input: "abcabcabcabc"
# Output: True
# Explanation: It's the substring "abc" four times. (And the substring "abcabc" 
# twice.)
#  
#  Related Topics String


# leetcode submit region begin(Prohibit modification and deletion)

def primes():
    yield 2
    p = 3
    while True:
        prime_found = True
        for x in primes():
            if p % x == 0:
                prime_found = False
                break
        if prime_found:
            yield p
        p += 1
        

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)

# leetcode submit region end(Prohibit modification and deletion)
