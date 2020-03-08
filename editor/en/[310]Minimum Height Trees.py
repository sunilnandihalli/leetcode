# For an undirected graph with tree characteristics, we can choose any node as t
# he root. The result graph is then a rooted tree. Among all possible rooted trees
# , those with minimum height are called minimum height trees (MHTs). Given such a
#  graph, write a function to find all the MHTs and return a list of their root la
# bels. 
# 
#  Format 
# The graph contains n nodes which are labeled from 0 to n - 1. You will be give
# n the number n and a list of undirected edges (each edge is a pair of labels). 
# 
#  You can assume that no duplicate edges will appear in edges. Since all edges 
# are undirected, [0, 1] is the same as [1, 0] and thus will not appear together i
# n edges. 
# 
#  Example 1 : 
# 
#  
# Input: n = 4, edges = [[1, 0], [1, 2], [1, 3]]
# 
#         0
#         |
#         1
#        / \
#       2   3 
# 
# Output: [1]
#  
# 
#  Example 2 : 
# 
#  
# Input: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
# 
#      0  1  2
#       \ | /
#         3
#         |
#         4
#         |
#         5 
# 
# Output: [3, 4] 
# 
#  Note: 
# 
#  
#  According to the definition of tree on Wikipedia: “a tree is an undirected gr
# aph in which any two vertices are connected by exactly one path. In other words,
#  any connected graph without simple cycles is a tree.” 
#  The height of a rooted tree is the number of edges on the longest downward pa
# th between the root and a leaf. 
#  
#  Related Topics Breadth-first Search Graph

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)

def test():
    ts = [(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]], [3, 4]),
          (4, [[1, 0], [1, 2], [1, 3]], [1])]
    s = Solution()
    for n, edges, ans in ts:
        actual = s.findMinHeightTrees(n, edges)
        print(n, edges, ans, actual)
        assert ans == actual


from collections import defaultdict
from functools import lru_cache


class Solution:
    def dfs(self, i, p):
        memo = {}
        if (i, p) in memo:
            return memo[(i, p)]
        m = 0
        for nei in self.neighbours[i]:
            if p != nei:
                m = max(self.dfs(nei, i), m)

        memo[(i, p)] = m + 1
        return m + 1

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        self.neighbours = defaultdict(list)
        for s, e in edges:
            self.neighbours[s].append(e)
            self.neighbours[e].append(s)

        same_height_roots = defaultdict(list)
        for i in range(n):
            same_height_roots[self.dfs(i, i)].append(i)

        return same_height_roots[min(same_height_roots.keys())]

# leetcode submit region end(Prohibit modification and deletion)
