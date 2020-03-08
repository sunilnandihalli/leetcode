# There is a ball in a maze with empty spaces and walls. The ball can go through
#  empty spaces by rolling up (u), down (d), left (l) or right (r), but it won't s
# top rolling until hitting a wall. When the ball stops, it could choose the next 
# direction. There is also a hole in this maze. The ball will drop into the hole i
# f it rolls on to the hole. 
# 
#  Given the ball position, the hole position and the maze, find out how the bal
# l could drop into the hole by moving the shortest distance. The distance is defi
# ned by the number of empty spaces traveled by the ball from the start position (
# excluded) to the hole (included). Output the moving directions by using 'u', 'd'
# , 'l' and 'r'. Since there could be several different shortest ways, you should 
# output the lexicographically smallest way. If the ball cannot reach the hole, ou
# tput "impossible". 
# 
#  The maze is represented by a binary 2D array. 1 means the wall and 0 means th
# e empty space. You may assume that the borders of the maze are all walls. The ba
# ll and the hole coordinates are represented by row and column indexes. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input 1: a maze represented by a 2D array
# 
# 0 0 0 0 0
# 1 1 0 0 1
# 0 0 0 0 0
# 0 1 0 0 1
# 0 1 0 0 0
# 
# Input 2: ball coordinate (rowBall, colBall) = (4, 3)
# Input 3: hole coordinate (rowHole, colHole) = (0, 1)
# 
# Output: "lul"
# 
# Explanation: There are two shortest ways for the ball to drop into the hole.
# The first way is left -> up -> left, represented by "lul".
# The second way is up -> left, represented by 'ul'.
# Both ways have shortest distance 6, but the first way is lexicographically sma
# ller because 'l' < 'u'. So the output is "lul".
# 
#  
# 
#  Example 2: 
# 
#  
# Input 1: a maze represented by a 2D array
# 
# 0 0 0 0 0
# 1 1 0 0 1
# 0 0 0 0 0
# 0 1 0 0 1
# 0 1 0 0 0
# 
# Input 2: ball coordinate (rowBall, colBall) = (4, 3)
# Input 3: hole coordinate (rowHole, colHole) = (3, 0)
# 
# Output: "impossible"
# 
# Explanation: The ball cannot reach the hole.
# 
#  
# 
#  
# 
#  Note: 
# 
#  
#  There is only one ball and one hole in the maze. 
#  Both the ball and hole exist on an empty space, and they will not be at the s
# ame position initially. 
#  The given maze does not contain border (like the red rectangle in the example,
#  pictures), but you could assume the border of the maze are all walls. 
#  The maze contains at least 2 empty spaces, and the width and the height of th
# e maze won't exceed 30. 
#  
#  Related Topics Depth-first Search Breadth-first Search

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
import heapq as h

dxdy = {'u': (-1, 0), 'd': (1, 0), 'l': (0, -1), 'r': (0, 1)}


def move(m, p, q, dir, s, e):
    assert s != e
    dx, dy = dxdy[dir]
    x, y = s
    ex, ey = e
    cost = 0
    while True:
        xn, yn = x + dx, y + dy
        if xn < 0 or xn == p or yn < 0 or yn == q or m[xn][yn] == 1:
            return (x, y), cost, False
        else:
            x = xn
            y = yn
            cost += 1
            if x == ex and y == ey:
                return (x, y), cost, True


def fsw(m, p, q, s, e):
    inf = (999999999, 'zzzzzzzz')

    memo = {s: (0, '')}
    front = [(0, '', s)]
    while len(front) > 0:
        cur_hcost, cur_hpath, cur = h.heappop(front)
        cur_cost, cur_path = memo[cur]
        for dir in 'dlru':
            next_loc, cost, goal_reached = move(m, p, q, dir, cur, e)
            v_new = cur_cost + cost, cur_path + dir
            if next_loc in memo:
                v_old = memo.get(next_loc)
                if v_old > v_new:
                    memo[next_loc] = v_new
            else:
                memo[next_loc] = v_new
                if not goal_reached:
                    h.heappush(front, (v_new[0], v_new[1], next_loc))

    return memo[e][1] if e in memo else 'impossible'


class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        p = len(maze)
        q = len(maze[0])
        return fsw(maze, p, q, tuple(ball), tuple(hole))


# leetcode submit region end(Prohibit modification and deletion)

def test():
    ts = [
        ([[0, 0, 0, 0, 0], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 1, 0, 0, 0]], (4, 3), (0, 1), 'lul'),
        ([[0, 0, 0, 0, 0], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 1, 0, 0, 0]], (4, 3), (3, 0),
         'impossible')]
    s = Solution()
    for m,ball,hole,ans in ts:
        actual = s.findShortestWay(m,ball,hole)
        print(actual,ans)
        assert actual==ans
