# Given a set of points in the xy-plane, determine the minimum area of a rectang
# le formed from these points, with sides parallel to the x and y axes. 
# 
#  If there isn't any rectangle, return 0. 
# 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
# Output: 4
#  
# 
#  
#  Example 2: 
# 
#  
# Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
# Output: 2
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= points.length <= 500 
#  0 <= points[i][0] <= 40000 
#  0 <= points[i][1] <= 40000 
#  All points are distinct. 
#  
#  
#  Related Topics Hash Table


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        
# leetcode submit region end(Prohibit modification and deletion)
