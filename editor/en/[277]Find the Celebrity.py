# Suppose you are at a party with n people (labeled from 0 to n - 1) and among t
# hem, there may exist one celebrity. The definition of a celebrity is that all th
# e other n - 1 people know him/her but he/she does not know any of them. 
# 
#  Now you want to find out who the celebrity is or verify that there is not one
# . The only thing you are allowed to do is to ask questions like: "Hi, A. Do you 
# know B?" to get information of whether A knows B. You need to find out the celeb
# rity (or verify there is not one) by asking as few questions as possible (in the
#  asymptotic sense). 
# 
#  You are given a helper function bool knows(a, b) which tells you whether A kn
# ows B. Implement a function int findCelebrity(n). There will be exactly one cele
# brity if he/she is in the party. Return the celebrity's label if there is a cele
# brity in the party. If there is no celebrity, return -1. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: graph = [
#   [1,1,0],
#   [0,1,0],
#   [1,1,1]
# ]
# Output: 1
# Explanation: There are three persons labeled with 0, 1 and 2. graph[i][j] = 1 
# means person i knows person j, otherwise graph[i][j] = 0 means person i does not
#  know person j. The celebrity is the person labeled as 1 because both 0 and 2 kn
# ow him but 1 does not know anybody.
#  
# 
#  Example 2: 
# 
#  
# Input: graph = [
#   [1,0,1],
#   [1,1,0],
#   [0,1,1]
# ]
# Output: -1
# Explanation: There is no celebrity.
#  
# 
#  
# 
#  Note: 
# 
#  
#  The directed graph is represented as an adjacency matrix, which is an n x n m
# atrix where a[i][j] = 1 means person i knows person j while a[i][j] = 0 means th
# e contrary. 
#  Remember that you won't have direct access to the adjacency matrix. 
#  
#  Related Topics Array


# leetcode submit region begin(Prohibit modification and deletion)
# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:
from functools import lru_cache

class Solution:

    @lru_cache(None)
    def mknows(self,a, b):
        self.num_knows_calls+=1
        return knows(a,b)

    def findCelebrity(self, n: int) -> int:
        self.num_knows_calls = 0
        may_be_celebs = set(range(n))
        while len(may_be_celebs)>0:
            x = may_be_celebs.pop()
            celeb = True
            for i in range(n):
                if i != x:
                    if not self.mknows(i,x):
                        celeb = False
                        break
                    else:
                        if i in may_be_celebs:
                            may_be_celebs.remove(i)
            if celeb:
                for i in range(n):
                    if i!= x:
                        if self.mknows(x,i):
                            celeb = False
                            break
            if celeb:
                return x
        return -1

# leetcode submit region end(Prohibit modification and deletion)
