# 
#  The demons had captured the princess (P) and imprisoned her in the bottom-rig
# ht corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D gri
# d. Our valiant knight (K) was initially positioned in the top-left room and must
#  fight his way through the dungeon to rescue the princess. 
# 
#  The knight has an initial health point represented by a positive integer. If 
# at any point his health point drops to 0 or below, he dies immediately. 
# 
#  Some of the rooms are guarded by demons, so the knight loses health (negative
#  integers) upon entering these rooms; other rooms are either empty (0's) or cont
# ain magic orbs that increase the knight's health (positive integers). 
# 
#  In order to reach the princess as quickly as possible, the knight decides to 
# move only rightward or downward in each step. 
# 
#  
# 
#  Write a function to determine the knight's minimum initial health so that he 
# is able to rescue the princess. 
# 
#  For example, given the dungeon below, the initial health of the knight must b
# e at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN. 
# 
#  
#  
#  
#  -2 (K) 
#  -3 
#  3 
#  
#  
#  -5 
#  -10 
#  1 
#  
#  
#  10 
#  30 
#  -5 (P) 
#  
#  
#  
# 
#  
# 
#  Note: 
# 
#  
#  The knight's health has no upper bound. 
#  Any room can contain threats or power-ups, even the first room the knight ent
# ers and the bottom-right room where the princess is imprisoned. 
#  
#  Related Topics Binary Search Dynamic Programming


# leetcode submit region begin(Prohibit modification and deletion)
from functools import lru_cache


@lru_cache(None)
def mhp(x, i, j, p, q):
    print(i, j)
    if i == p or j == q:
        return float('-inf'), 0
    else:
        min_health_i, total_health_i = mhp(x, i + 1, j, p, q)
        min_health_j, total_health_j = mhp(x, i, j + 1, p, q)

        new_min_health_i = max(min_health_i, total_health_i + x[i][j])
        new_min_health_j = max(min_health_j, total_health_j + x[i][j])
        if new_min_health_i > new_min_health_j:
            return new_min_health_i, total_health_i + x[i][j]
        elif new_min_health_j > new_min_health_i:
            return new_min_health_j, total_health_j + x[i][j]
        elif total_health_i > total_health_j:
            return new_min_health_i, total_health_i
        else:
            return new_min_health_j, total_health_j


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = tuple([tuple(x) for x in dungeon])
        p = len(m)
        q = len(m[0]) if p > 0 else 0
        for i in range(p - 1, -1, -1):
            for j in range(q - 1, -1, -1):
                h, th = mhp(m, i, j, p, q)
        return -h if h < 0 else 0
# leetcode submit region end(Prohibit modification and deletion)
