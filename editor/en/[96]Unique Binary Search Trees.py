# Given n, how many structurally unique BST's (binary search trees) that store v
# alues 1 ... n? 
# 
#  Example: 
# 
#  
# Input: 3
# Output: 5
# Explanation:
# Given n = 3, there are a total of 5 unique BST's:
# 
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
#  
#  Related Topics Dynamic Programming Tree


# leetcode submit region begin(Prohibit modification and deletion)
from functools import lru_cache


@lru_cache(None)
def num_trees(n):
    if n == 0:
        return 1
    else:
        return sum([num_trees(i) * num_trees(n - i - 1) for i in range(n)])


class Solution:
    def numTrees(self, n: int) -> int:
        for i in range(n):
            num_trees(i)
        return num_trees(n)


def test():
    ts = [(3, 5)]
    s = Solution()
    for n, ans in ts:
        actual = s.numTrees(n)
        print(n, ans, actual)
        assert ans == actual
# leetcode submit region end(Prohibit modification and deletion)
