# Say you have an array for which the i-th element is the price of a given stock
#  on day i. 
# 
#  Design an algorithm to find the maximum profit. You may complete at most k tr
# ansactions. 
# 
#  Note: 
# You may not engage in multiple transactions at the same time (ie, you must sel
# l the stock before you buy again). 
# 
#  Example 1: 
# 
#  
# Input: [2,4,1], k = 2
# Output: 2
# Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 
# 4-2 = 2.
#  
# 
#  Example 2: 
# 
#  
# Input: [3,2,6,5,0,3], k = 2
# Output: 7
# Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 
# 6-2 = 4.
#              Then buy on day 5 (price = 0) and sell on day 6 (price = 3), prof
# it = 3-0 = 3.
#  
#  Related Topics Dynamic Programming


# leetcode submit region begin(Prohibit modification and deletion)

trough = 'trough'
peak = 'peak'


def turning_points(x):
    ret = []
    i = 0
    peak_type = trough
    while i < len(x):
        if peak_type == trough:
            while i < len(x) - 1 and x[i + 1] <= x[i]:
                i += 1
            ret.append((i, trough))
            peak_type = peak
        else:
            while i < len(x) - 1 and x[i + 1] >= x[i]:
                i += 1
            ret.append((i, peak))
            peak_type = trough
        i += 1
    return ret


import heapq as h


def max_profit(prices, num_transactions):
    tp = turning_points(prices)
    if len(tp) > 0:
        if tp[-1][1] == trough:
            tp.pop()
    while len(tp) > num_transactions * 2:
        i = 0
        min_loss_i = None
        min_loss = None
        while i < len(tp) - 1:
            if min_loss is None or min_loss > abs(prices[tp[i][0]] - prices[tp[i + 1][0]]):
                min_loss = abs(prices[tp[i][0]] - prices[tp[i + 1][0]])
                min_loss_i = i
            i += 1
        tp = tp[:min_loss_i] + tp[min_loss_i + 2:]
    ret = 0
    for i in range(0, len(tp), 2):
        ret += prices[tp[i + 1][0]] - prices[tp[i][0]]
    return ret


def test_turning_points():
    ts = [([0, 0, 1, 2, 3, 2, 1, 2, 3, 3, 4, -1, -1],
           [(1, trough), (4, peak), (6, trough), (10, peak), (12, trough)])]
    for arr, ans in ts:
        actual = turning_points(arr)
        print(arr, ans, actual)
        assert actual == ans


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        return max_profit(prices, k)
    # leetcode submit region end(Prohibit modification and deletion)
