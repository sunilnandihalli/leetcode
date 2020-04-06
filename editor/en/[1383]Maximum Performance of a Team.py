# There are n engineers numbered from 1 to n and two arrays: speed and efficienc
# y, where speed[i] and efficiency[i] represent the speed and efficiency for the i
# -th engineer respectively. Return the maximum performance of a team composed of 
# at most k engineers, since the answer can be a huge number, return this modulo 1
# 0^9 + 7. 
# 
#  The performance of a team is the sum of their engineers' speeds multiplied by
#  the minimum efficiency among their engineers. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2
# Output: 60
# Explanation: 
# We have the maximum performance of the team by selecting engineer 2 (with spee
# d=10 and efficiency=4) and engineer 5 (with speed=5 and efficiency=7). That is, 
# performance = (10 + 5) * min(4, 7) = 60.
#  
# 
#  Example 2: 
# 
#  
# Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3
# Output: 68
# Explanation:
# This is the same example as the first but k = 3. We can select engineer 1, eng
# ineer 2 and engineer 5 to get the maximum performance of the team. That is, perf
# ormance = (2 + 10 + 5) * min(5, 4, 7) = 68.
#  
# 
#  Example 3: 
# 
#  
# Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4
# Output: 72
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 10^5 
#  speed.length == n 
#  efficiency.length == n 
#  1 <= speed[i] <= 10^5 
#  1 <= efficiency[i] <= 10^8 
#  1 <= k <= n 
#  Related Topics Greedy Sort

def test():
    ts = [(6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 2, 60),
          (6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 3, 68),
          (6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 4, 72)]
    for n, speed, efficiency, k, ans in ts:
        s = Solution()
        actual = s.maxPerformance(n, speed, efficiency, k)
        print(n, speed, efficiency, k, ans, actual)
        assert actual == ans


from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        workers = sorted((-s,e))

    def maxPerformanceOld(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        best_speed_people = sorted(range(n), key=lambda x: (speed[x], efficiency[x]))
        best_efficiency_people = sorted(range(n), key=lambda x: (efficiency[x], speed[x]))
        best_product_people = sorted(range(n), key=lambda x: efficiency[x] * speed[x])
        productive_people = set([])
        cur_min_efficiency = float('inf')
        cur_speed_sum = 0
        cur_productivity = 0
        while len(productive_people) < k:
            while best_speed_people[-1] in productive_people:
                best_speed_people.pop()
            speed_person = best_speed_people[-1]
            while best_efficiency_people[-1] in productive_people:
                best_efficiency_people.pop()
            efficiency_person = best_efficiency_people[-1]
            while best_product_people[-1] in productive_people:
                best_product_people.pop()
            product_person = best_product_people[-1]
            best_new_person = None
            best_new_productivity = cur_productivity
            print('cur_productivity : ', cur_productivity, ' cur_min_efficiency : ', cur_min_efficiency,
                  ' cur_speed_sum : ', cur_speed_sum)
            for p in set([speed_person, efficiency_person, product_person]):
                productivity = (cur_speed_sum + speed[p]) * min(cur_min_efficiency, efficiency[p])
                if best_new_productivity < productivity:
                    best_new_person = p
                    best_new_productivity = productivity
                print('best_new_productivity : ', best_new_productivity, 'best_new_person : ', best_new_person)
            if best_new_person is not None:
                productive_people.add(best_new_person)
                cur_productivity = best_new_productivity
                cur_speed_sum += speed[best_new_person]
                cur_min_efficiency = min(cur_min_efficiency, efficiency[best_new_person])
                print('choice : ', productive_people)
            else:
                break
        print([(p, speed[p], efficiency[p]) for p in productive_people])

        return cur_productivity

# leetcode submit region end(Prohibit modification and deletion)
