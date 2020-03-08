# Find the kth largest element in an unsorted array. Note that it is the kth lar
# gest element in the sorted order, not the kth distinct element. 
# 
#  Example 1: 
# 
#  
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
#  
# 
#  Example 2: 
# 
#  
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4 
# 
#  Note: 
# You may assume k is always valid, 1 ≤ k ≤ array's length. 
#  Related Topics Divide and Conquer Heap


# leetcode submit region begin(Prohibit modification and deletion)
import heapq as h
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = [-x for x in nums]
        h.heapify(arr)
        ans = 0
        for i in range(k):
            ans = h.heappop(arr)
        return -ans

# leetcode submit region end(Prohibit modification and deletion)
