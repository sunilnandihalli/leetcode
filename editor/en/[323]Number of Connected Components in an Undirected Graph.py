# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edg
# e is a pair of nodes), write a function to find the number of connected componen
# ts in an undirected graph. 
# 
#  Example 1: 
# 
#  
# Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]
# 
#      0          3
#      |          |
#      1 --- 2    4 
# 
# Output: 2
#  
# 
#  Example 2: 
# 
#  
# Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
# 
#      0           4
#      |           |
#      1 --- 2 --- 3
# 
# Output:  1
#  
# 
#  Note: 
# You can assume that no duplicate edges will appear in edges. Since all edges a
# re undirected, [0, 1] is the same as [1, 0] and thus will not appear together in
#  edges. 
#  Related Topics Depth-first Search Breadth-first Search Union Find Graph
from typing import List
def test():
    ts = [(5, [[0, 1], [1, 2], [3, 4]], 2), (5, [[0, 1], [1, 2], [2, 3], [3, 4]], 1)]
    s = Solution()
    for n, edges, ans in ts:
        actual = s.countComponents(n, edges)
        print(n, edges, ans, actual)
        assert actual == ans


# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        g = {i: [] for i in range(n)}
        for s, e in edges:
            g[s].append(e)
            g[e].append(s)

        components = []
        while len(g) > 0:
            node_id, neighs = g.popitem()
            cur_component = set([node_id])
            front = set(neighs)
            while len(front) > 0:
                node_id = front.pop()
                cur_component.add(node_id)
                for x in g[node_id]:
                    if x not in cur_component and x not in front:
                        front.add(x)
                del g[node_id]
            components.append(cur_component)
        return len(components)
# leetcode submit region end(Prohibit modification and deletion)
