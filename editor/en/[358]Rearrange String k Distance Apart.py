# Given a non-empty string s and an integer k, rearrange the string such that th
# e same characters are at least distance k from each other. 
# 
#  All input strings are given in lowercase letters. If it is not possible to re
# arrange the string, return an empty string "". 
# 
#  Example 1: 
# 
#  
#  
# Input: s = "aabbcc", k = 3
# Output: "abcabc" 
# Explanation: The same letters are at least distance 3 from each other.
#  
# 
#  
#  Example 2: 
# 
#  
# Input: s = "aaabc", k = 3
# Output: "" 
# Explanation: It is not possible to rearrange the string.
#  
# 
#  
#  Example 3: 
# 
#  
# Input: s = "aaadbbcc", k = 2
# Output: "abacabcd"
# Explanation: The same letters are at least distance 2 from each other.
#  
#  
#  
#  Related Topics Hash Table Heap Greedy
def test():
    s = Solution()
    ts = [('aabbcc', 3, 'abcabc'), ('aaabc', 3, ''), ('aaadbbcc', 2, 'abacabcd')]
    for arr, k, ans in ts:
        actual = s.rearrangeString(arr, k)
        print(arr, k, ans, ' actual : ', actual)
        assert ans == actual


from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter
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


import heapq as h


class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        pq = mpqdict(priority_precedes=lambda x, y: x > y)
        for character, cnt in Counter(s).items():
            pq[character] = cnt
        waiting = []
        ret = ''
        while len(pq) > 0:
            character, cnt = pq.popitem()
            ret += character
            if cnt > 1:
                h.heappush(waiting, (len(ret) - 1, (character, cnt - 1)))
            while len(waiting) > 0 and waiting[0][0] <= len(ret) - k:
                _, (character, cnt) = h.heappop(waiting)
                pq[character] = cnt
        return '' if len(waiting) > 0 else ret

# leetcode submit region end(Prohibit modification and deletion)
