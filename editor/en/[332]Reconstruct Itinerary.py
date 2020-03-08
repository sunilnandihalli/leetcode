# Given a list of airline tickets represented by pairs of departure and arrival 
# airports [from, to], reconstruct the itinerary in order. All of the tickets belo
# ng to a man who departs from JFK. Thus, the itinerary must begin with JFK. 
# 
#  Note: 
# 
#  
#  If there are multiple valid itineraries, you should return the itinerary that
#  has the smallest lexical order when read as a single string. For example, the i
# tinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"]. 
#  All airports are represented by three capital letters (IATA code). 
#  You may assume all tickets form at least one valid itinerary. 
#  
# 
#  Example 1: 
# 
#  
# Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
#  
# 
#  Example 2: 
# 
#  
# Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# 
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL"
# ,"SFO"].
#              But it is larger in lexical order.
#  
#  Related Topics Depth-first Search Graph
from typing import List


def test():
    ts = [([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]], ["JFK", "MUC", "LHR", "SFO", "SJC"]),
          ([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]],
           ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"])]
    s = Solution()
    for inp, ans in ts:
        actual = s.findItinerary(inp)
        print(inp, ans, actual)
        assert ans == actual


# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict
from copy import deepcopy


class Solution:
    def try_hop(self, cur_loc):
        tobe_tried_tickets = deepcopy(self.tkts[cur_loc])
        for i, tkt_id in enumerate(tobe_tried_tickets):
            next_loc = self.tickets[tkt_id][1]
            self.tkts[cur_loc] = tobe_tried_tickets[:i] + tobe_tried_tickets[i + 1:]
            self.stk.append(tkt_id)
            self.unused_tickets -= 1
            if self.unused_tickets == 0:
                return True
            elif self.try_hop(next_loc):
                return True
            else:
                self.stk.pop()
                self.unused_tickets += 1
                self.tkts[cur_loc] = tobe_tried_tickets
        return self.unused_tickets == 0

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.tickets = tickets
        self.stk = []
        self.tkts = defaultdict(list)
        for tkt_id, (s, _) in enumerate(tickets):
            self.tkts[s].append(tkt_id)
        self.unused_tickets = len(self.tickets)
        for x, y in self.tkts.items():
            y.sort(key=lambda tkt_id: tickets[tkt_id][1])

        self.try_hop('JFK')
        ret = ['JFK']
        for tkt_id in self.stk:
            ret.append(tickets[tkt_id][1])
        return ret

# leetcode submit region end(Prohibit modification and deletion)
