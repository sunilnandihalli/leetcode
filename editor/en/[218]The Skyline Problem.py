# A city's skyline is the outer contour of the silhouette formed by all the buil
# dings in that city when viewed from a distance. Now suppose you are given the lo
# cations and height of all the buildings as shown on a cityscape photo (Figure A)
# , write a program to output the skyline formed by these buildings collectively (
# Figure B). 
#  
# 
#  The geometric information of each building is represented by a triplet of int
# egers [Li, Ri, Hi], where Li and Ri are the x coordinates of the left and right 
# edge of the ith building, respectively, and Hi is its height. It is guaranteed t
# hat 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX, and Ri - Li > 0. You may assume all 
# buildings are perfect rectangles grounded on an absolutely flat surface at heigh
# t 0. 
# 
#  For instance, the dimensions of all buildings in Figure A are recorded as: [ 
# [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] . 
# 
#  The output is a list of "key points" (red dots in Figure B) in the format of 
# [ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline. A key poin
# t is the left endpoint of a horizontal line segment. Note that the last key poin
# t, where the rightmost building ends, is merely used to mark the termination of 
# the skyline, and always has zero height. Also, the ground in between any two adj
# acent buildings should be considered part of the skyline contour. 
# 
#  For instance, the skyline in Figure B should be represented as:[ [2 10], [3 1
# 5], [7 12], [12 0], [15 10], [20 8], [24, 0] ]. 
# 
#  Notes: 
# 
#  
#  The number of buildings in any input list is guaranteed to be in the range [0
# , 10000]. 
#  The input list is already sorted in ascending order by the left x position Li
# . 
#  The output list must be sorted by the x position. 
#  There must be no consecutive horizontal lines of equal height in the output s
# kyline. For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not accepta
# ble; the three lines of height 5 should be merged into one in the final output a
# s such: [...[2 3], [4 5], [12 7], ...] 
#  
#  Related Topics Divide and Conquer Heap Binary Indexed Tree Segment Tree Line 
# Sweep


# leetcode submit region begin(Prohibit modification and deletion)
import heapq as h

from collections import namedtuple

class pqdict:
    def __init__(self,elems_dict_,):

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        buildings = sorted(buildings)

# leetcode submit region end(Prohibit modification and deletion)
