# Given two lists of closed intervals, each list of intervals is pairwise disjoi
# nt and in sorted order. 
# 
#  Return the intersection of these two interval lists. 
# 
#  (Formally, a closed interval [a, b] (with a <= b) denotes the set of real num
# bers x with a <= x <= b. The intersection of two closed intervals is a set of re
# al numbers that is either empty, or can be represented as a closed interval. For
#  example, the intersection of [1, 3] and [2, 4] is [2, 3].) 
# 
#  
#  
# 
#  Example 1: 
# 
#  
# 
#  
# Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
# Reminder: The inputs and the desired output are lists of Interval objects, and
#  not arrays or lists.
#  
# 
#  
# 
#  Note: 
# 
#  
#  0 <= A.length < 1000 
#  0 <= B.length < 1000 
#  0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9 
#  
# 
#  NOTE: input types have been changed on April 15, 2019. Please reset to defaul
# t code definition to get new method signature. 
#  
#  Related Topics Two Pointers

from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
import heapq as h


def flattened_generator(arr, arr_id):
    for i, x in enumerate(arr):
        for j, y in enumerate(x):
            yield y, (j, arr_id)


def events(sorted_intervals_arrays):
    flattened_sorted_intervals_generators = [flattened_generator(x, i) for i, x in enumerate(sorted_intervals_arrays)]
    num_generators = len(flattened_sorted_intervals_generators)
    front = []
    for g in flattened_sorted_intervals_generators:
        try:
            x = next(g)
            front.append(x)
        except StopIteration:
            num_generators -= 1
    h.heapify(front)
    while len(front) > 0:
        y, (j,i) = h.heappop(front)
        yield y, (i, j)
        try:
            x = next(flattened_sorted_intervals_generators[i])
            h.heappush(front, x)
        except StopIteration:
            num_generators -= 1


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        available_people = set()
        num_people = 2
        ret = []
        start = None
        for ts, (i, j) in events([A, B]):
            if j == 0:
                available_people.add(i)
                if len(available_people) == num_people:
                    start = ts
            else:
                if start is not None:
                    ret.append([start, ts])
                    start = None
                available_people.remove(i)
        return ret


# leetcode submit region end(Prohibit modification and deletion)

def test():
    ts = [([[0, 2], [5, 10], [13, 23], [24, 25]],
           [[1, 5], [8, 12], [15, 24], [25, 26]],
           [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]])]
    s = Solution()
    for a, b, ans in ts:
        actual = s.intervalIntersection(a, b)
        print(a, b, ans, actual)
        assert ans == actual
