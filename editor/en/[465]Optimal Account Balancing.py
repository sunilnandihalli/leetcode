# A group of friends went on holiday and sometimes lent each other money. For ex
# ample, Alice paid for Bill's lunch for $10. Then later Chris gave Alice $5 for a
#  taxi ride. We can model each transaction as a tuple (x, y, z) which means perso
# n x gave person y $z. Assuming Alice, Bill, and Chris are person 0, 1, and 2 res
# pectively (0, 1, 2 are the person's ID), the transactions can be represented as 
# [[0, 1, 10], [2, 0, 5]]. 
# 
#  Given a list of transactions between a group of people, return the minimum nu
# mber of transactions required to settle the debt. 
# 
#  Note:
#  
#  A transaction will be given as a tuple (x, y, z). Note that x ≠ y and z > 0. 
# 
#  Person's IDs may not be linear, e.g. we could have the persons 0, 1, 2 or we 
# could also have the persons 0, 2, 6. 
#  
#  
# 
#  Example 1:
#  
# Input:
# [[0,1,10], [2,0,5]]
# 
# Output:
# 2
# 
# Explanation:
# Person #0 gave person #1 $10.
# Person #2 gave person #0 $5.
# 
# Two transactions are needed. One way to settle the debt is person #1 pays pers
# on #0 and #2 $5 each.
#  
#  
# 
#  Example 2:
#  
# Input:
# [[0,1,10], [1,0,1], [1,2,5], [2,0,5]]
# 
# Output:
# 1
# 
# Explanation:
# Person #0 gave person #1 $10.
# Person #1 gave person #0 $1.
# Person #1 gave person #2 $5.
# Person #2 gave person #0 $5.
# 
# Therefore, person #1 only need to give person #0 $4, and all debt is settled.
#  
#
from typing import List


def test():
    ts = [([[0, 1, 10], [2, 0, 5]], 2),
          ([[0, 1, 10], [1, 0, 1], [1, 2, 5], [2, 0, 5]], 1),
          ([[10, 11, 6], [12, 13, 7], [14, 15, 2], [14, 16, 2], [14, 17, 2], [14, 18, 2]], 6)]
    for transactions, ans in ts:
        s = Solution()
        actual = s.minTransfers(transactions)
        print(transactions, ans, actual)
        assert actual == ans


# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict
import heapq as h


class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        return self.minTransfersHeap(transactions)
    
    def minTransfersHeap(self, transactions: List[List[int]]) -> int:
        recievables = defaultdict(int)
        for lender, borrower, amount in transactions:
            recievables[lender] += amount
            recievables[borrower] -= amount
        lenders = []
        borrowers = []
        for person, amount in recievables.items():
            if amount > 0:
                lenders.append((-amount, person))
            elif amount < 0:
                borrowers.append((amount, person))
        h.heapify(lenders)
        h.heapify(borrowers)
        num_transactions = 0
        while len(lenders) > 0 or len(borrowers) > 0:
            print('lenders   : ', lenders)
            print('borrowers : ', borrowers)
            neg_lender_amount, cur_largest_lender = h.heappop(lenders)
            neg_borrower_amount, cur_largest_borrower = h.heappop(borrowers)
            lender_amount = -neg_lender_amount
            borrower_amount = -neg_borrower_amount

            if borrower_amount > lender_amount:
                h.heappush(borrowers, (-(borrower_amount - lender_amount), cur_largest_borrower))
            elif lender_amount > borrower_amount:
                h.heappush(lenders, (-(lender_amount - borrower_amount), cur_largest_lender))
            num_transactions += 1

        return num_transactions
# leetcode submit region end(Prohibit modification and deletion)
