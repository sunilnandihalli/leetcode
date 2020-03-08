# Median is the middle value in an ordered integer list. If the size of the list
#  is even, there is no middle value. So the median is the mean of the two middle 
# value. 
# Examples:
# 
#  [2,3,4] , the median is 3 
# 
#  [2,3], the median is (2 + 3) / 2 = 2.5 
# 
#  Given an array nums, there is a sliding window of size k which is moving from
#  the very left of the array to the very right. You can only see the k numbers in
#  the window. Each time the sliding window moves right by one position. Your job 
# is to output the median array for each window in the original array. 
# 
#  For example, 
# Given nums = [1,3,-1,-3,5,3,6,7], and k = 3. 
# 
#  
# Window position                Median
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       1
#  1 [3  -1  -3] 5  3  6  7       -1
#  1  3 [-1  -3  5] 3  6  7       -1
#  1  3  -1 [-3  5  3] 6  7       3
#  1  3  -1  -3 [5  3  6] 7       5
#  1  3  -1  -3  5 [3  6  7]      6
#  
# 
#  Therefore, return the median sliding window as [1,-1,-1,3,5,6]. 
# 
#  Note: 
# You may assume k is always valid, ie: k is always smaller than input array's s
# ize for non-empty array. 
# Answers within 10^-5 of the actual value will be accepted as correct. 
#  Related Topics Sliding Window


# leetcode submit region begin(Prohibit modification and deletion)
import heapq as h
def get_max(max_heap):


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        s = 0
        e = k
        elems = [(x, i) for i, x in enumerate(x)]
        kelems = sorted(elems[:e])
        ret = []
        if k % 2 == 0:
            left_heap = h.heapify([(-x, i) for x, i in kelems[:k // 2]])
            right_heap = h.heapify(kelems[k // 2:])
            ret.append(median)
            while e<len(nums):
                s+=1


                e+=1
        else:
            median = kelems[k // 2]
            left_heap = h.heapify([(-x, i) for x, i in kelems[:k // 2]])
            right_heap = h.heapify(kelems[k // 2 + 1:])

# leetcode submit region end(Prohibit modification and deletion)
