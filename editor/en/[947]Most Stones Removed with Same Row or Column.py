# On a 2D plane, we place stones at some integer coordinate points. Each coordin
# ate point may have at most one stone. 
# 
#  Now, a move consists of removing a stone that shares a column or row with ano
# ther stone on the grid. 
# 
#  What is the largest possible number of moves we can make? 
# 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
# Output: 5
#  
# 
#  
#  Example 2: 
# 
#  
# Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
# Output: 3
#  
# 
#  
#  Example 3: 
# 
#  
# Input: stones = [[0,0]]
# Output: 0
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= stones.length <= 1000 
#  0 <= stones[i][j] < 10000 
#  
#  
#  
#  
#  Related Topics Depth-first Search Union Find


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
# leetcode submit region end(Prohibit modification and deletion)
