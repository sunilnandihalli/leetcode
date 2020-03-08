# Say you have an array for which the ith element is the price of a given stock 
# on day i. 
# 
#  Design an algorithm to find the maximum profit. You may complete at most two 
# transactions. 
# 
#  Note: You may not engage in multiple transactions at the same time (i.e., you
#  must sell the stock before you buy again). 
# 
#  Example 1: 
# 
#  
# Input: [3,3,5,0,0,3,1,4]
# Output: 6
# Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 
# 3-0 = 3.
#              Then buy on day 7 (price = 1) and sell on day 8 (price = 4), prof
# it = 4-1 = 3. 
# 
#  Example 2: 
# 
#  
# Input: [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 
# 5-1 = 4.
#              Note that you cannot buy on day 1, buy on day 2 and sell them lat
# er, as you are
#              engaging multiple transactions at the same time. You must sell be
# fore buying again.
#  
# 
#  Example 3: 
# 
#  
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0. 
#  Related Topics Array Dynamic Programming
from typing import List


def test():
    ts = [([3, 3, 5, 0, 0, 3, 1, 4], 6), ([1, 2, 3, 4, 5], 4), ([], 0)]
    s = Solution()
    for prices, ans in ts:
        actual = s.maxProfit(prices)
        print(prices, ans, actual)
        assert actual == ans


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
    def maxProfit(self, prices: List[int]) -> int:
        return max_profit(prices, 2)
# leetcode submit region end(Prohibit modification and deletion)
