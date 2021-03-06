# Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge 
# is a pair of nodes), write a function to check whether these edges make up a val
# id tree. 
# 
#  Example 1: 
# 
#  
# Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
# Output: true 
# 
#  Example 2: 
# 
#  
# Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
# Output: false 
# 
#  Note: you can assume that no duplicate edges will appear in edges. Since all 
# edges are undirected, [0,1] is the same as [1,0] and thus will not appear togeth
# er in edges. 
#  Related Topics Depth-first Search Breadth-first Search Union Find Graph

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
def test():
    ts = [(5, [[0, 1], [0, 2], [0, 3], [1, 4]], True),
          (5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], False),
          (5, [[0, 1], [0, 4], [1, 4], [2, 3]], False)]
    s = Solution()
    for n, edges, ans in ts:
        actual = s.validTree(n, edges)
        print(n, edges, ans, actual)
        assert actual == ans


from collections import defaultdict


class mpqdict():
    def __init__(self, priority_keyfn=lambda x: x, priority_precedes=lambda x, y: x < y):
        self.heap = []
        self.dict = {}
        self.priority_precedes = priority_precedes
        self.priority_keyfn = priority_keyfn

    def __setitem__(self, key, value):
        # print('inserting ', key, value)
        if key in self.dict:
            ind = self.dict[key]
            _, old_value = self.heap[ind]
            self.heap[self.dict[key]] = (key, value)
            if self.priority_precedes(self.priority_keyfn(old_value), self.priority_keyfn(value)):
                self.bubble_down(ind)
            else:
                self.bubble_up(ind)
        else:
            self.heap.append((key, value))
            self.dict[key] = len(self.heap) - 1
            self.bubble_up(len(self.heap) - 1)

    def __contains__(self, key):
        return key in self.dict

    def __getitem__(self, key):
        return self.heap[self.dict[key]][1]

    def __len__(self):
        return len(self.heap)

    def _swap(self, i, j):
        ki, vi = self.heap[i]
        kj, vj = self.heap[j]
        self.heap[j] = ki, vi
        self.heap[i] = kj, vj
        self.dict[ki] = j
        self.dict[kj] = i

    def bubble_down(self, i):
        # print('bubble_down %d' % i + self.__repr__())
        k, v = self.heap[i]
        il = 2 * i + 1
        ir = 2 * i + 2
        lk, lv = self.heap[il] if il < len(self.heap) else (None, None)
        rk, rv = self.heap[ir] if ir < len(self.heap) else (None, None)
        # print((lk, lv), (rk, rv))
        if lk and rk:
            if self.priority_precedes(self.priority_keyfn(lv), self.priority_keyfn(rv)):
                if self.priority_precedes(self.priority_keyfn(lv), self.priority_keyfn(v)):
                    self._swap(il, i)
                    self.bubble_down(il)
            elif self.priority_precedes(self.priority_keyfn(rv), self.priority_keyfn(v)):
                self._swap(ir, i)
                self.bubble_down(ir)
        elif lk:
            if self.priority_precedes(self.priority_keyfn(lv), self.priority_keyfn(v)):
                self._swap(il, i)

    def bubble_up(self, i):
        # print('bubble_up %d' % i + self.__repr__())
        if i > 0:
            k, v = self.heap[i]
            p = (i - 1) // 2
            pk, pv = self.heap[p]
            if self.priority_precedes(self.priority_keyfn(v), self.priority_keyfn(pv)):
                self._swap(p, i)
                self.bubble_up(p)

    def __repr__(self):
        return '%s %s' % (self.heap.__repr__(), self.dict.__repr__())

    def popitem(self):
        if len(self.heap) > 0:
            self._swap(0, len(self.heap) - 1)
            k, v = self.heap.pop()
            del self.dict[k]
            if self.__len__() > 0:
                self.bubble_down(0)
            return k, v
        else:
            return None

from collections import Counter

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        graph = [-1]*n

        def find(u):
            while graph[u]!=-1:
                u = graph[u]
            return u

        for s,e in edges:
            s_graph = find(s)
            e_graph = find(e)
            if s_graph==e_graph:
                return False
            else:
                graph[s_graph] = e_graph

        return Counter(graph)[-1]==1



    def validDirectedGraph(self, n, edges):
        if len(edges) != n - 1:
            return False
        out_edges = defaultdict(list)
        in_edges = mpqdict()
        for i in range(n):
            in_edges[i] = 0
        for s, e in edges:
            out_edges[s].append(e)
            in_edges[e] += 1
        while len(in_edges) > 0:
            node_id, cnt = in_edges.popitem()
            if cnt != 0:
                return False
            for e in out_edges[node_id]:
                in_edges[e] -= 1
        return True

# leetcode submit region end(Prohibit modification and deletion)
