# Given a char array representing tasks CPU need to do. It contains capital lett
# ers A to Z where different letters represent different tasks. Tasks could be don
# e without original order. Each task could be done in one interval. For each inte
# rval, CPU could finish one task or just be idle. 
# 
#  However, there is a non-negative cooling interval n that means between two sa
# me tasks, there must be at least n intervals that CPU are doing different tasks 
# or just be idle. 
# 
#  You need to return the least number of intervals the CPU will take to finish 
# all the given tasks. 
# 
#  
# 
#  Example: 
# 
#  
# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
#  
# 
#  
# 
#  Note: 
# 
#  
#  The number of tasks is in the range [1, 10000]. 
#  The integer n is in the range [0, 100]. 
#  
#  Related Topics Array Greedy Queue
from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter
import heapq as h


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tc = Counter(tasks)
        task_heap = [(-cnt, task) for task, cnt in tc.items()]
        h.heapify(task_heap)

        intervals = 0
        cooling_tasks_heap = []
        while len(task_heap) > 0 or len(cooling_tasks_heap) > 0:
            if len(task_heap) > 0:
                neg_cnt, task = h.heappop(task_heap)
                if neg_cnt < -1:
                    h.heappush(cooling_tasks_heap, (intervals, neg_cnt + 1, task))
            while len(cooling_tasks_heap) > 0:
                last_run_interval, neg_cnt, task = cooling_tasks_heap[0]
                if last_run_interval + n <= intervals:
                    h.heappop(cooling_tasks_heap)
                    h.heappush(task_heap, (neg_cnt, task))
                else:
                    break
            intervals += 1
        return intervals


# leetcode submit region end(Prohibit modification and deletion)

def test():
    ts = [('AAABBB', 2, 8)]
    s = Solution()
    for tasks, n, ans in ts:
        actual = s.leastInterval(tasks, n)
        print(tasks, n, ans, actual)
        assert actual == ans
