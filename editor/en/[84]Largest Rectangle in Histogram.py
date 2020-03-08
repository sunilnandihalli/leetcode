# Given n non-negative integers representing the histogram's bar height where th
# e width of each bar is 1, find the area of largest rectangle in the histogram. 
# 
#  
# 
#  
# Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3
# ]. 
# 
#  
# 
#  
# The largest rectangle is shown in the shaded area, which has area = 10 unit. 
# 
#  
# 
#  Example: 
# 
#  
# Input: [2,1,5,6,2,3]
# Output: 10
#  
#  Related Topics Array Stack



# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

# leetcode submit region end(Prohibit modification and deletion)
def test():
    ts = [([2,1,5,6,2,3],10)]
