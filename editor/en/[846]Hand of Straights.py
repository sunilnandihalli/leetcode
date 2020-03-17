# Alice has a hand of cards, given as an array of integers. 
# 
#  Now she wants to rearrange the cards into groups so that each group is size W
# , and consists of W consecutive cards. 
# 
#  Return true if and only if she can. 
# 
#  
# 
#  
#  
# 
#  Example 1: 
# 
#  
# Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
# Output: true
# Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]. 
# 
#  Example 2: 
# 
#  
# Input: hand = [1,2,3,4,5], W = 4
# Output: false
# Explanation: Alice's hand can't be rearranged into groups of 4. 
# 
#  
# 
#  Note: 
# 
#  
#  1 <= hand.length <= 10000 
#  0 <= hand[i] <= 10^9 
#  1 <= W <= hand.length 
#  
#  Related Topics Ordered Map
def test():
    ts = [([1, 2, 3, 6, 2, 3, 4, 7, 8], 3, True), ([1, 2, 3, 4, 5], 4, False),
          ([6, 7, 5, 3, 4, 7, 8, 10, 9, 6], 5, True)]
    for arr, w, ans in ts:
        s = Solution()
        actual = s.isNStraightHand(arr, w)
        print(arr, w, ans, actual)
        assert actual == ans


from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
import heapq as h


class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if W == 1:
            return True
        hand = sorted(hand)
        incomplete_groups = []
        for x in hand:

        return len(incomplete_groups) == 0
# leetcode submit region end(Prohibit modification and deletion)
