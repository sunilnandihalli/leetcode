# Implement a MyCalendar class to store your events. A new event can be added if
#  adding the event will not cause a double booking. 
# 
#  Your class will have the method, book(int start, int end). Formally, this rep
# resents a booking on the half open interval [start, end), the range of real numb
# ers x such that start <= x < end. 
# 
#  A double booking happens when two events have some non-empty intersection (ie
# ., there is some time that is common to both events.) 
# 
#  For each call to the method MyCalendar.book, return true if the event can be 
# added to the calendar successfully without causing a double booking. Otherwise, 
# return false and do not add the event to the calendar. 
# Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCale
# ndar.book(start, end)
# 
#  Example 1: 
# 
#  
# MyCalendar();
# MyCalendar.book(10, 20); // returns true
# MyCalendar.book(15, 25); // returns false
# MyCalendar.book(20, 30); // returns true
# Explanation: 
# The first event can be booked.  The second can't because time 15 is already bo
# oked by another event.
# The third event can be booked, as the first event takes every time less than 2
# 0, but not including 20.
#  
# 
#  
# 
#  Note: 
# 
#  
#  The number of calls to MyCalendar.book per test case will be at most 1000. 
#  In calls to MyCalendar.book(start, end), start and end are integers in the ra
# nge [0, 10^9]. 
#  
# 
#  
#  Related Topics Array


# leetcode submit region begin(Prohibit modification and deletion)
from bisect import bisect_left


class MyCalendar:

    def __init__(self):
        self.intervals = []

    def book(self, start: int, end: int) -> bool:
        i = bisect_left(self.intervals, (start, end))
        if i > 0:
            prev_interval = self.intervals[i - 1]
            if prev_interval[1] > start:
                return False

        if i < len(self.intervals):
            next_interval = self.intervals[i]
            if next_interval[0] < end:
                return False

        self.intervals = self.intervals[:i] + [(start, end)] + self.intervals[i:]
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
# leetcode submit region end(Prohibit modification and deletion)
