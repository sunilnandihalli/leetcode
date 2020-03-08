# Given an undirected graph, return true if and only if it is bipartite. 
# 
#  Recall that a graph is bipartite if we can split it's set of nodes into two i
# ndependent subsets A and B such that every edge in the graph has one node in A a
# nd another node in B. 
# 
#  The graph is given in the following form: graph[i] is a list of indexes j for
#  which the edge between nodes i and j exists. Each node is an integer between 0 
# and graph.length - 1. There are no self edges or parallel edges: graph[i] does n
# ot contain i, and it doesn't contain any element twice. 
# 
#  
# Example 1:
# Input: [[1,3], [0,2], [1,3], [0,2]]
# Output: true
# Explanation: 
# The graph looks like this:
# 0----1
# |    |
# |    |
# 3----2
# We can divide the vertices into two groups: {0, 2} and {1, 3}.
#  
# 
#  
# Example 2:
# Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
# Output: false
# Explanation: 
# The graph looks like this:
# 0----1
# | \  |
# |  \ |
# 3----2
# We cannot find a way to divide the set of nodes into two independent subsets.
#  
# 
#  
# 
#  Note: 
# 
#  
#  graph will have length in range [1, 100]. 
#  graph[i] will contain integers in range [0, graph.length - 1]. 
#  graph[i] will not contain i or duplicate values. 
#  The graph is undirected: if any element j is in graph[i], then i will be in g
# raph[j]. 
#  
#  Related Topics Depth-first Search Breadth-first Search Graph
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        tobevisited = set(range(n))
        flags = {}
        while len(tobevisited) > 0:
            cur = tobevisited.pop()
            front = [cur]
            flags[cur] = 0
            while len(front) > 0:
                cur = front.pop()
                cur_flag = flags[cur]
                nei_flag = 1 if cur_flag == 0 else 0
                neighbors = graph[cur]
                for nei in neighbors:
                    if nei in flags:
                        if flags[nei] != nei_flag:
                            return False
                    else:
                        tobevisited.remove(nei)
                        flags[nei] = nei_flag
                        front.insert(0, nei)
        return True


# leetcode submit region end(Prohibit modification and deletion)

def test():
    ts = [([[1, 3], [0, 2], [1, 3], [0, 2]], True),
          ([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]], False),
          ([[], [2, 4, 6], [1, 4, 8, 9], [7, 8], [1, 2, 8, 9], [6, 9], [1, 5, 7, 8, 9], [3, 6, 9], [2, 3, 4, 6, 9],
            [2, 4, 5, 6, 7, 8]], False)]
    s = Solution()
    for g, ans in ts:
        actual = s.isBipartite(g)
        print(g, ans, actual)
        assert (ans == actual)
