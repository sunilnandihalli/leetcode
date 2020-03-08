# Given the edges of a directed graph, and two nodes source and destination of t
# his graph, determine whether or not all paths starting from source eventually en
# d at destination, that is: 
# 
#  
#  At least one path exists from the source node to the destination node 
#  If a path exists from the source node to a node with no outgoing edges, then 
# that node is equal to destination. 
#  The number of possible paths from source to destination is a finite number. 
#  
# 
#  Return true if and only if all roads from source lead to destination. 
# 
#  
# 
#  Example 1: 
# 
#  
# 
#  
# Input: n = 3, edges = [[0,1],[0,2]], source = 0, destination = 2
# Output: false
# Explanation: It is possible to reach and get stuck on both node 1 and node 2.
#  
# 
#  Example 2: 
# 
#  
# 
#  
# Input: n = 4, edges = [[0,1],[0,3],[1,2],[2,1]], source = 0, destination = 3
# Output: false
# Explanation: We have two possibilities: to end at node 3, or to loop over node
#  1 and node 2 indefinitely.
#  
# 
#  Example 3: 
# 
#  
# 
#  
# Input: n = 4, edges = [[0,1],[0,2],[1,3],[2,3]], source = 0, destination = 3
# Output: true
#  
# 
#  Example 4: 
# 
#  
# 
#  
# Input: n = 3, edges = [[0,1],[1,1],[1,2]], source = 0, destination = 2
# Output: false
# Explanation: All paths from the source node end at the destination node, but t
# here are an infinite number of paths, such as 0-1-2, 0-1-1-2, 0-1-1-1-2, 0-1-1-1
# -1-2, and so on.
#  
# 
#  Example 5: 
# 
#  
# 
#  
# Input: n = 2, edges = [[0,1],[1,1]], source = 0, destination = 1
# Output: false
# Explanation: There is infinite self-loop at destination node.
#  
# 
#  
# 
#  Note: 
# 
#  
#  The given graph may have self loops and parallel edges. 
#  The number of nodes n in the graph is between 1 and 10000 
#  The number of edges in the graph is between 0 and 10000 
#  0 <= edges.length <= 10000 
#  edges[i].length == 2 
#  0 <= source <= n - 1 
#  0 <= destination <= n - 1 
#  
#  Related Topics Depth-first Search Graph
from typing import List


def test():
    ts = [(2, [[0, 1], [1, 1]], 0, 1, False),
          (3, [[0, 1], [1, 1], [1, 2]], 0, 2, False),
          (4, [[0, 1], [0, 2], [1, 3], [2, 3]], 0, 3, True),
          (4, [[0, 1], [0, 3], [1, 2], [2, 1]], 0, 3, False),
          (3, [[0, 1], [0, 2]], 0, 2, False)]
    s = Solution()
    for n, edges, src, dst, ans in ts:
        actual = s.leadsToDestination(n, edges, src, dst)
        print(n, edges, src, dst, ans, actual)
        assert ans == actual


# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict


class Solution:

    def dfs(self, node_id):
        self.visited.add(node_id)
        if node_id != self.destination and len(self.out_edges[node_id]) == 0:
            return False
        else:
            for nei in self.out_edges[node_id]:
                if nei in self.visited or not self.dfs(nei):
                    return False
        self.visited.remove(node_id)
        return True

    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        self.out_edges = {}
        for i in range(n):
            self.out_edges[i] = []

        for s, e in edges:
            self.out_edges[s].append(e)

        if len(self.out_edges[destination]) > 0:
            return False

        self.destination = destination
        self.visited = set()
        return self.dfs(source)

# leetcode submit region end(Prohibit modification and deletion)
