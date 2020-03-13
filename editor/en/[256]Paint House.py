# There are a row of n houses, each house can be painted with one of the three c
# olors: red, blue or green. The cost of painting each house with a certain color 
# is different. You have to paint all the houses such that no two adjacent houses 
# have the same color. 
# 
#  The cost of painting each house with a certain color is represented by a n x 
# 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with col
# or red; costs[1][2] is the cost of painting house 1 with color green, and so on.
# .. Find the minimum cost to paint all houses. 
# 
#  Note: 
# All costs are positive integers. 
# 
#  Example: 
# 
#  
# Input: [[17,2,17],[16,16,5],[14,3,19]]
# Output: 10
# Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 
# into blue. 
#              Minimum cost: 2 + 5 + 3 = 10.
#  
#  Related Topics Dynamic Programming


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        if n == 0:
            return 0
        dp = [[0] * 3 for _ in range(len(costs))]
        for house_id in range(len(costs)):
            for color in range(3):
                dp[house_id][color] = costs[0][color] if house_id == 0 else costs[house_id][color] + min(
                    dp[house_id - 1][(color + 1) % 3], dp[house_id - 1][(color + 2) % 3])

        return min(dp[n - 1])

# leetcode submit region end(Prohibit modification and deletion)
