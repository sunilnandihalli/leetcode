# 
# In this problem, a tree is an undirected graph that is connected and has no cy
# cles.
#  
# The given input is a graph that started as a tree with N nodes (with distinct 
# values 1, 2, ..., N), with one additional edge added. The added edge has two dif
# ferent vertices chosen from 1 to N, and was not an edge that already existed.
#  
# The resulting graph is given as a 2D-array of edges. Each element of edges is 
# a pair [u, v] with u < v, that represents an undirected edge connecting nodes u 
# and v.
#  
# Return an edge that can be removed so that the resulting graph is a tree of N 
# nodes. If there are multiple answers, return the answer that occurs last in the 
# given 2D-array. The answer edge [u, v] should be in the same format, with u < v.
# 
#  Example 1: 
#  
# Input: [[1,2], [1,3], [2,3]]
# Output: [2,3]
# Explanation: The given undirected graph will be like this:
#   1
#  / \
# 2 - 3
#  
#  
#  Example 2: 
#  
# Input: [[1,2], [2,3], [3,4], [1,4], [1,5]]
# Output: [1,4]
# Explanation: The given undirected graph will be like this:
# 5 - 1 - 2
#     |   |
#     4 - 3
#  
#  
#  Note: 
#  The size of the input 2D-array will be between 3 and 1000. 
#  Every integer represented in the 2D-array will be between 1 and N, where N is
#  the size of the input array. 
#  
# 
#  
# 
#  
# Update (2017-09-26): 
# We have overhauled the problem description + test cases and specified clearly 
# the graph is an undirected graph. For the directed graph follow up please see Re
# dundant Connection II). We apologize for any inconvenience caused.
#  Related Topics Tree Union Find Graph
from typing import List


def test():
    ts = [([[9, 10], [5, 8], [2, 6], [1, 5], [3, 8], [4, 9], [8, 10], [4, 10], [6, 8], [7, 9]], [4, 10]),
          ([[1, 2], [1, 3], [2, 3]], [2, 3]),
          ([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]], [1, 4])]
    s = Solution()
    for inp, ans in ts:
        actual = s.findRedundantConnection(inp)
        print(inp, ans, actual)
        assert ans == actual


# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict


def print_inp_out(f):
    def ret(inp):
        output = f(inp)
        print('priority_keyfn : input ', inp, ' output : ', output)
        return output

    return ret


class mpqdict():

    def __init__(self, priority_keyfn=lambda x: x, priority_precedes=lambda x, y: x < y):
        self.heap = []
        self.dict = {}
        self.priority_precedes = priority_precedes
        self.priority_keyfn = print_inp_out(priority_keyfn)

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

    def update(self, key, update_fn):
        self.__setitem__(key, update_fn(self.heap[self.dict.get(key)][1] if key in self.dict else None))

    def topitem(self):
        return self.heap[0]

    def items(self):
        return self.heap

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


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        neighbours = mpqdict(priority_keyfn=len)

        def add_node(x):
            def f(mp):
                c_node_id, c_edge_id = x
                mp = mp or {}
                mp[c_node_id] = c_edge_id
                return mp

            return f

        def remove_node(x):
            def f(mp):
                c_node_id, c_edge_id = x
                del mp[c_node_id]
                return mp

            return f

        for i, (s, e) in enumerate(edges):
            neighbours.update(s, add_node((e, i)))
            neighbours.update(e, add_node((s, i)))

        while len(neighbours) > 0:
            print(neighbours)
            print(neighbours.popitem())

        while len(neighbours) > 2:
            k, neis = neighbours.topitem()
            if len(neis) == 1:
                neighbours.popitem()
                for nei_node, nei_edge_id in neis.items():
                    remove_fn = remove_node((k, nei_edge_id))
                    neighbours.update(nei_node, remove_fn)
            else:
                print(neighbours)
                max_edge_id = None
                for node_id, out_edges in neighbours.items():
                    print(len(out_edges))
                    for out_edge_node_id, edge_id in out_edges.items():
                        max_edge_id = max(max_edge_id, edge_id) if max_edge_id else edge_id
                return edges[max_edge_id]
        return None
# leetcode submit region end(Prohibit modification and deletion)
