# There are a row of n houses, each house can be painted with one of the k color
# s. The cost of painting each house with a certain color is different. You have t
# o paint all the houses such that no two adjacent houses have the same color. 
# 
#  The cost of painting each house with a certain color is represented by a n x 
# k cost matrix. For example, costs[0][0] is the cost of painting house 0 with col
# or 0; costs[1][2] is the cost of painting house 1 with color 2, and so on... Fin
# d the minimum cost to paint all houses. 
# 
#  Note: 
# All costs are positive integers. 
# 
#  Example: 
# 
#  
# Input: [[1,5,3],[2,9,4]]
# Output: 5
# Explanation: Paint house 0 into color 0, paint house 1 into color 2. Minimum c
# ost: 1 + 4 = 5; 
#              Or paint house 0 into color 2, paint house 1 into color 0. Minimu
# m cost: 3 + 2 = 5. 
#  
# 
#  Follow up: 
# Could you solve it in O(nk) runtime? 
#  Related Topics Dynamic Programming


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        
# leetcode submit region end(Prohibit modification and deletion)
