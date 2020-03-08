# Given an unsorted array of integers, find the length of longest increasing sub
# sequence. 
# 
#  Example: 
# 
#  
# Input: [10,9,2,5,3,7,101,18]
# Output: 4 
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the 
# length is 4. 
# 
#  Note: 
# 
#  
#  There may be more than one LIS combination, it is only necessary for you to r
# eturn the length. 
#  Your algorithm should run in O(n2) complexity. 
#  
# 
#  Follow up: Could you improve it to O(n log n) time complexity? 
#  Related Topics Binary Search Dynamic Programming
from typing import List
from hypothesis import given, strategies as st, example
# leetcode submit region begin(Prohibit modification and deletion)

from functools import lru_cache


@lru_cache(None)
def llcs(a, b, i, j):
    if i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            return 1 + llcs(a, b, i - 1, j - 1)
        else:
            return max(llcs(a, b, i - 1, j), llcs(a, b, i, j - 1))
    else:
        return 0


@lru_cache(None)
def lcs_helper(a, b, i, j):
    if i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            return lcs_helper(a, b, i - 1, j - 1) + [a[i - 1]]
        elif llcs(a, b, i - 1, j) > llcs(a, b, i, j - 1):
            return lcs_helper(a, b, i - 1, j)
        else:
            return lcs_helper(a, b, i, j - 1)
    else:
        return []


def lcs(a, b):
    return lcs_helper(a, b, len(a), len(b))


def lis(arr):
    sarray = sorted(arr)
    return lcs(tuple(arr), tuple(sarray))

def llis(arr):
    return llcs(tuple(arr),tuple(sorted(arr)))

import bisect as b


def to_list(x):
    if x is None:
        return []
    first, rest = x
    return to_list(rest) + [first]


def lisnlogn(arr):
    if len(arr) > 0:
        cur_lis = []
        cur_tuples = []
        inc_seqs = []
        for i, x in enumerate(arr):
            loc = b.bisect_right(cur_lis, x)
            if loc < len(cur_lis):
                inc_seqs.append((len(cur_lis), cur_tuples[-1]))
            cur_lis = cur_lis[:loc] + [x]
            cur_tuples = cur_tuples[:loc] + [(x, cur_tuples[loc - 1] if loc > 0 else None)]
        inc_seqs.append((len(cur_lis), cur_tuples[-1]))
        return to_list(max(inc_seqs)[1])
    else:
        return arr


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        return len(lisnlogn(nums))


# leetcode submit region end(Prohibit modification and deletion)
@given(arr=st.lists(st.integers()))
@example([10, 9, 2, 5, 3, 7, 101, 18])
@example([1, 1, 0, 1])
def test(arr):
    dp_nlogn_ans = lisnlogn(arr)
    lcs_ans = lis(arr)
    print(arr, dp_nlogn_ans, lcs_ans)
    assert len(dp_nlogn_ans) == len(lcs_ans)
