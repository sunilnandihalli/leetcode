# Given an array nums sorted in ascending order, return true if and only if you 
# can split it into 1 or more subsequences such that each subsequence consists of 
# consecutive integers and has length at least 3. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: [1,2,3,3,4,5]
# Output: True
# Explanation:
# You can split them into two consecutive subsequences : 
# 1, 2, 3
# 3, 4, 5
# 
#  
# 
#  Example 2: 
# 
#  
# Input: [1,2,3,3,4,4,5,5]
# Output: True
# Explanation:
# You can split them into two consecutive subsequences : 
# 1, 2, 3, 4, 5
# 3, 4, 5
# 
#  
# 
#  Example 3: 
# 
#  
# Input: [1,2,3,4,4,5]
# Output: False
#  
# 
#  
# 
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10000 
#  
# 
#  
#  Related Topics Heap Greedy

def test():
    ts = [([1, 2, 3, 3, 4, 5], True), ([1, 2, 3, 3, 4, 4, 5, 5], True), ([1, 2, 3, 4, 4, 5], False)]
    for arr, ans in ts:
        s = Solution()
        print(arr)
        actual = s.isPossible(arr)
        print(arr, ans, actual)
        assert ans == actual


from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
import heapq as h


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        subseqs = []
        last, neg_start = None, None
        for x in nums:
            while len(subseqs) > 0:
                last, neg_start = subseqs[0]
                if last + 1 < x:
                    if neg_start + last + 1 < 3:
                        return False
                    last, neg_start = None, None
                    h.heappop(subseqs)
                elif last + 1 == x:
                    h.heappop(subseqs)
                    break
                else:
                    last, neg_start = None, None
                    break
            nxt_push = (x, neg_start if neg_start is not None else -x)
            h.heappush(subseqs, nxt_push)
        while len(subseqs) > 0:
            last, neg_start = h.heappop(subseqs)
            if neg_start + last + 1 < 3:
                return False
        return True
# leetcode submit region end(Prohibit modification and deletion)
