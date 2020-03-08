# Think about Zuma Game. You have a row of balls on the table, colored red(R), y
# ellow(Y), blue(B), green(G), and white(W). You also have several balls in your h
# and. 
# 
#  Each time, you may choose a ball in your hand, and insert it into the row (in
# cluding the leftmost place and rightmost place). Then, if there is a group of 3 
# or more balls in the same color touching, remove these balls. Keep doing this un
# til no more balls can be removed. 
# 
#  Find the minimal balls you have to insert to remove all the balls on the tabl
# e. If you cannot remove all the balls, output -1. 
# 
#  
#  Example 1: 
# 
#  
# Input: board = "WRRBBW", hand = "RB"
# Output: -1
# Explanation: WRRBBW -> WRR[R]BBW -> WBBW -> WBB[B]W -> WW
#  
# 
#  Example 2: 
# 
#  
# Input: board = "WWRRBBWW", hand = "WRBRW"
# Output: 2
# Explanation: WWRRBBWW -> WWRR[R]BBWW -> WWBBWW -> WWBB[B]WW -> WWWW -> empty
#  
# 
#  Example 3: 
# 
#  
# Input: board = "G", hand = "GGGGG"
# Output: 2
# Explanation: G -> G[G] -> GG[G] -> empty 
#  
# 
#  Example 4: 
# 
#  
# Input: board = "RBYYBBRRB", hand = "YRBGB"
# Output: 3
# Explanation: RBYYBBRRB -> RBYY[Y]BBRRB -> RBBBRRB -> RRRB -> B -> B[B] -> BB[B
# ] -> empty 
#  
# 
#  
#  Constraints: 
# 
#  
#  You may assume that the initial row of balls on the table won’t have any 3 or
#  more consecutive balls with the same color. 
#  The number of balls on the table won't exceed 16, and the string represents t
# hese balls is called "board" in the input. 
#  The number of balls in your hand won't exceed 5, and the string represents th
# ese balls is called "hand" in the input. 
#  Both input strings will be non-empty and only contain characters 'R','Y','B',
# 'G','W'. 
#  
#  Related Topics Depth-first Search


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        
# leetcode submit region end(Prohibit modification and deletion)
