# Given a string S, check if the letters can be rearranged so that two character
# s that are adjacent to each other are not the same. 
# 
#  If possible, output any possible result. If not possible, return the empty st
# ring. 
# 
#  Example 1: 
# 
#  
# Input: S = "aab"
# Output: "aba"
#  
# 
#  Example 2: 
# 
#  
# Input: S = "aaab"
# Output: ""
#  
# 
#  Note: 
# 
#  
#  S will consist of lowercase letters and have length in range [1, 500]. 
#  
# 
#  
#  Related Topics String Heap Greedy Sort

def test():
    ts = [('baaba', 'ababa')]
    for inp, out in ts:
        s = Solution()
        actual = s.reorganizeString(inp)
        print(inp, out, actual)
        assert out == actual


# leetcode submit region begin(Prohibit modification and deletion)
import heapq as h
from collections import Counter


class Solution:
    def reorganizeString(self, S: str) -> str:
        character_counts = Counter(S)
        available_heap = [(-count, character) for character, count in character_counts.items()]
        h.heapify(available_heap)
        waiting_char = None
        ret = []
        while len(available_heap) > 0:
            neg_cnt, character = h.heappop(available_heap)
            ret.append(character)
            if waiting_char:
                h.heappush(available_heap, waiting_char)
            waiting_char = (neg_cnt + 1, character) if neg_cnt + 1 != 0 else None
        return ''.join(ret) if waiting_char is None else ''
# leetcode submit region end(Prohibit modification and deletion)
