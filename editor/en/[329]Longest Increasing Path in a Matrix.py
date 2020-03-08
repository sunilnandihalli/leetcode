# Given an integer matrix, find the length of the longest increasing path. 
# 
#  From each cell, you can either move to four directions: left, right, up or do
# wn. You may NOT move diagonally or move outside of the boundary (i.e. wrap-aroun
# d is not allowed). 
# 
#  Example 1: 
# 
#  
# Input: nums = 
# [
#   [9,9,4],
#   [6,6,8],
#   [2,1,1]
# ] 
# Output: 4 
# Explanation: The longest increasing path is [1, 2, 6, 9].
#  
# 
#  Example 2: 
# 
#  
# Input: nums = 
# [
#   [3,4,5],
#   [3,2,6],
#   [2,2,1]
# ] 
# Output: 4 
# Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is
#  not allowed.
#  
#  Related Topics Depth-first Search Topological Sort Memoization

from typing import List
import pqdict


def mpqdict():
    return pqdict.pqdict()


# leetcode submit region begin(Prohibit modification and deletion)

from collections import defaultdict


class mpqdict():
    def __init__(self, priority_keyfn=lambda x: x, priority_precedes=lambda x, y: x < y):
        self.heap = []
        self.dict = {}
        self.priority_precedes = priority_precedes
        self.priority_keyfn = priority_keyfn

    def __setitem__(self, key, value):
        #print('inserting ', key, value)
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
        #print('bubble_down %d' % i + self.__repr__())
        k, v = self.heap[i]
        il = 2 * i + 1
        ir = 2 * i + 2
        lk, lv = self.heap[il] if il < len(self.heap) else (None, None)
        rk, rv = self.heap[ir] if ir < len(self.heap) else (None, None)
        #print((lk, lv), (rk, rv))
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
        #print('bubble_up %d' % i + self.__repr__())
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
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        p = len(matrix)
        if p > 0:
            q = len(matrix[0])
        else:
            return 0
        up = 'up'
        down = 'down'
        right = 'right'
        left = 'left'
        dirs = {up: (-1, 0), down: (1, 0), right: (0, 1), left: (0, -1)}

        def node(node_id, dir):
            i, j = node_id
            i1 = i + dir[0]
            j1 = j + dir[1]
            if 0 <= i1 < p and 0 <= j1 < q:
                return i1, j1

        def val(node_id, dir):
            if node(node_id, dir):
                i1, j1 = node(node_id, dir)
                return matrix[i1][j1]

        def out_edges(node_id):
            i, j = node_id
            for dir in dirs.values():
                if node(node_id, dir) and val(node_id, dir) > matrix[i][j]:
                    yield node(node_id, dir)

        def in_edges(node_id):
            i, j = node_id
            for dir in dirs.values():
                if node(node_id, dir) and val(node_id, dir) < matrix[i][j]:
                    yield node(node_id, dir)

        num_in_edges = mpqdict()
        for i in range(p):
            for j in range(q):
                node_id = (i, j)
                num_in_edges[node_id] = len(list(in_edges(node_id)))

        topo_order = []
        while len(num_in_edges) > 0:
            node_id, in_edge_cnt = num_in_edges.popitem()
            topo_order.append(node_id)
            for out_edge_node in out_edges(node_id):
                num_in_edges[out_edge_node] -= 1

        max_length = 0
        path_length = defaultdict(int)
        for node_id in topo_order:
            for in_edge_node in in_edges(node_id):
                path_length[node_id] = max(path_length[in_edge_node] + 1, path_length[node_id])
            max_length = max(path_length[node_id], max_length)

        return max_length + 1
        # leetcode submit region end(Prohibit modification and deletion)


def testmpq():
    ts = [({10: 20, 20: 5, 30: 40}, [], [(20, 5), (10, 20), (30, 40)]),
          ({10: 20, 20: 5, 30: 40}, [(30, 1), (20, 21)], [(30, 1), (10, 20), (20, 21)])]
    x = mpqdict()
    for m, updates, ans in ts:
        for k, v in m.items():
            x[k] = v
            print(x)

        for k, v in updates:
            x[k] = v
            print(x)

        for k_ans, v_ans in ans:
            k, v = x.popitem()
            print('popping k_ans : %d v_ans : %d k : %d v : %d' % (k_ans, v_ans, k, v))
            assert k == k_ans
            assert v == v_ans
        assert len(x) == 0


def test():
    ts = [([[9, 9, 4], [6, 6, 8], [2, 1, 1]], 4),
          ([[3, 4, 5], [3, 2, 6], [2, 2, 1]], 4)]
    for m, ans in ts:
        s = Solution()
        actual = s.longestIncreasingPath(m)
        print(m, ans, actual)
        assert ans == actual
