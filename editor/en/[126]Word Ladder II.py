# Given two words (beginWord and endWord), and a dictionary's word list, find al
# l shortest transformation sequence(s) from beginWord to endWord, such that: 
# 
#  
#  Only one letter can be changed at a time 
#  Each transformed word must exist in the word list. Note that beginWord is not
#  a transformed word. 
#  
# 
#  Note: 
# 
#  
#  Return an empty list if there is no such transformation sequence. 
#  All words have the same length. 
#  All words contain only lowercase alphabetic characters. 
#  You may assume no duplicates in the word list. 
#  You may assume beginWord and endWord are non-empty and are not the same. 
#  
# 
#  Example 1: 
# 
#  
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
# 
# Output:
# [
#   ["hit","hot","dot","dog","cog"],
#   ["hit","hot","lot","log","cog"]
# ]
#  
# 
#  Example 2: 
# 
#  
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# 
# Output: []
# 
# Explanation: The endWord "cog" is not in wordList, therefore no possible trans
# formation.
#  
# 
#  
#  
#  Related Topics Array String Backtracking Breadth-first Search

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict, namedtuple

FrontElem = namedtuple('FrontElem', 'cost word')
PathElem = namedtuple('PathElem', 'cost prev')

import heapq as h


def gen_hashes(word):
    for i in range(len(word)):
        yield word[:i] + '.' + word[i + 1:]


def create_graph(ws):
    graph = defaultdict(list)
    for w in ws:
        for h in gen_hashes(w):
            graph[h].append(w)
    return graph


def flatten_path(x):
    ret = []
    while x != ():
        ret.append(x[0])
        x = x[1]
    return list(reversed(ret))


def find_paths(s, e, words):
    g = create_graph(words)
    paths = {s: PathElem(0, [()])}
    front = [FrontElem(0, s)]
    while len(front) > 0:
        _, cur = h.heappop(front)
        cur_path = paths[cur]
        new_v = PathElem(cur_path.cost + 1, [tuple([cur, x]) for x in cur_path.prev])
        for x in gen_hashes(cur):
            for nei in g[x]:
                if nei != cur:
                    if nei in paths:
                        old_v = paths[nei]
                        if old_v.cost > new_v.cost:
                            paths[nei] = new_v
                        elif old_v.cost == new_v.cost:
                            paths[nei] = PathElem(new_v.cost, h.merge(old_v.prev, new_v.prev))
                    else:
                        paths[nei] = new_v
                        if nei != e:
                            h.heappush(front, FrontElem(new_v.cost, nei))
    ret = []
    if e in paths:
        for p in paths[e].prev:
            r = flatten_path(p)
            r.append(e)
            ret.append(r)
    return ret


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        return find_paths(beginWord, endWord, wordList)


# leetcode submit region end(Prohibit modification and deletion)
def test():
    ts = [('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log'], []),
          ('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog'],
           [['hit', 'hot', 'dot', 'dog', 'cog'], ['hit', 'hot', 'lot', 'log', 'cog']])]
    sol = Solution()
    for s, e, dictionary, ans in ts:
        actual = sol.findLadders(s, e, dictionary)
        print(actual, ans)
        assert (actual == ans)
