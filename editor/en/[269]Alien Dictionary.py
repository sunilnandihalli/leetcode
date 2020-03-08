# There is a new alien language which uses the latin alphabet. However, the orde
# r among letters are unknown to you. You receive a list of non-empty words from t
# he dictionary, where words are sorted lexicographically by the rules of this new
#  language. Derive the order of letters in this language. 
# 
#  Example 1: 
# 
#  
# Input:
# [
#   "wrt",
#   "wrf",
#   "er",
#   "ett",
#   "rftt"
# ]
# 
# Output: "wertf"
#  
# 
#  Example 2: 
# 
#  
# Input:
# [
#   "z",
#   "x"
# ]
# 
# Output: "zx"
#  
# 
#  Example 3: 
# 
#  
# Input:
# [
#   "z",
#   "x",
#   "z"
# ] 
# 
# Output: "" 
# 
# Explanation: The order is invalid, so return "".
#  
# 
#  Note: 
# 
#  
#  You may assume all letters are in lowercase. 
#  You may assume that if a is a prefix of b, then a must appear before b in the
#  given dictionary. 
#  If the order is invalid, return an empty string. 
#  There may be multiple valid order of letters, return any one of them is fine.
#  
#  
#  Related Topics Graph Topological Sort
from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        i = 1
        directed_edges = []
        while i < len(words):
            s1 = words[i - 1]
            s2 = words[i]
            j = 0
            while j < min(len(s1), len(s2)) and s1[j] == s2[j]:
                j += 1
            if j < min(len(s1), len(s2)):
                directed_edges.append((s1[j], s2[j]))
            i += 1
        zero_in_degree = set()
        in_degree = {}
        for w in words:
            for c in w:
                zero_in_degree.add(c)
                in_degree[c] = 0
        outward_endpoints = defaultdict(list)
        for s, e in directed_edges:
            in_degree[e] += 1
            if e in zero_in_degree:
                zero_in_degree.remove(e)
            outward_endpoints[s].append(e)
        ordering = []
        while len(zero_in_degree) > 0:
            x = zero_in_degree.pop()
            del in_degree[x]
            for nei in outward_endpoints[x]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    zero_in_degree.add(nei)
            ordering.append(x)
        return ''.join(ordering if len(in_degree) == 0 else [])


# leetcode submit region end(Prohibit modification and deletion)

def test():
    ts = [(["wrt", "wrf", "er", "ett", "rftt"], 'wertf'), (['z', 'x', 'z'], ''),(["ac","ab","b"],'acb')]
    s = Solution()
    for dictionary, ans in ts:
        actual = s.alienOrder(dictionary)
        print(ans, actual)
        assert ans == actual
