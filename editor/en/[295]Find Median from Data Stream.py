# Median is the middle value in an ordered integer list. If the size of the list
#  is even, there is no middle value. So the median is the mean of the two middle 
# value. 
# For example,
# 
#  [2,3,4], the median is 3 
# 
#  [2,3], the median is (2 + 3) / 2 = 2.5 
# 
#  Design a data structure that supports the following two operations: 
# 
#  
#  void addNum(int num) - Add a integer number from the data stream to the data 
# structure. 
#  double findMedian() - Return the median of all elements so far. 
#  
# 
#  
# 
#  Example: 
# 
#  
# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3) 
# findMedian() -> 2
#  
# 
#  
# 
#  Follow up: 
# 
#  
#  If all integer numbers from the stream are between 0 and 100, how would you o
# ptimize it? 
#  If 99% of all integer numbers from the stream are between 0 and 100, how woul
# d you optimize it? 
#  
#  Related Topics Heap Design
from statistics import median
from random import randint


def test():
    last_n = 5
    x = MedianFinder(last_n)
    l = []
    for _ in range(1000):
        num = randint(0, 999)
        l.append(num)
        x.addNum(num)
        expected = median(l[-last_n:])
        actual = x.findMedian()
        print(len(l), x, l, expected, actual)
        assert expected == actual


def st():
    last_n = 5
    ts = [712, 434, 292, 358, 73, 830, 664, 815]
    mf = MedianFinder(last_n)
    l = []
    for x in ts:
        mf.addNum(x)
        l.append(x)
        expected = median(l[-last_n:])
        actual = mf.findMedian()
        print(len(l), mf, l, expected, actual)
        assert expected == actual


# leetcode submit region begin(Prohibit modification and deletion)
import heapq as h


class MedianFinder:

    def __init__(self, last_n=None):
        """
        initialize your data structure here.
        """
        self.min_heap = []
        self.max_heap = []
        self.min_heap_count = 0
        self.max_heap_count = 0
        self.added_count = 0
        self.last_n = last_n
        if self.last_n is not None:
            self.elems = {}
        self.last_valid_index = 0

    def peek_max_heap(self):
        if self.max_heap_count > 0:
            neg_num, index = self.max_heap[0]
            while index < self.last_valid_index:
                h.heappop(self.max_heap)
                neg_num, index = self.max_heap[0]
            return -neg_num, index

    def peek_min_heap(self):
        if self.min_heap_count > 0:
            num, index = self.min_heap[0]
            while index < self.last_valid_index:
                h.heappop(self.min_heap)
                num, index = self.min_heap[0]
            return num, index

    def pop_max_heap_element(self):
        if self.max_heap_count > 0:
            num, index = self.peek_max_heap()
            h.heappop(self.max_heap)
            self.max_heap_count -= 1
            return num, index

    def push_max_heap_element(self, num, index):
        h.heappush(self.max_heap, (-num, index))
        self.max_heap_count += 1

    def pop_min_heap_element(self):
        if self.min_heap_count > 0:
            num, index = self.peek_min_heap()
            h.heappop(self.min_heap)
            self.min_heap_count -= 1
            return num, index

    def push_min_heap_element(self, num, index):
        h.heappush(self.min_heap, (num, index))
        self.min_heap_count += 1

    def rebalance(self):
        if self.max_heap_count > self.min_heap_count + 1:
            while self.max_heap_count > self.min_heap_count + 1:
                num, index = self.pop_max_heap_element()
                self.push_min_heap_element(num, index)
        elif self.max_heap_count < self.min_heap_count:
            while self.max_heap_count < self.min_heap_count:
                num, index = self.pop_min_heap_element()
                self.push_max_heap_element(num, index)

    def __repr__(self):
        return 'max_heap {} min_heap {} last_valid_index {} max_heap_count {} min_heap_count {}'.format(self.max_heap,
                                                                                                        self.min_heap,
                                                                                                        self.last_valid_index,
                                                                                                        self.max_heap_count,
                                                                                                        self.min_heap_count)

    def remove_oldest_element(self):
        v_max, i_max = self.peek_max_heap()
        v_min, i_min = self.peek_min_heap()
        v = self.elems[self.last_valid_index]
        e_max = (-v_max, i_max)
        e_min = (v_min, i_min)
        le_max = (-v, self.last_valid_index)
        le_min = (v, self.last_valid_index)
        if le_max >= e_max:
            self.max_heap_count -= 1
        elif le_min >= e_min:
            self.min_heap_count -= 1
        del self.elems[self.last_valid_index]
        self.last_valid_index += 1

    def addNum(self, num: int) -> None:
        if self.last_n is not None and self.added_count - self.last_valid_index == self.last_n:
            self.remove_oldest_element()
        if self.max_heap_count > 0:
            v_max, i_max = self.peek_max_heap()
            e_max = (-v_max, i_max)
            ne_max = (-num, self.added_count)
            if ne_max >= e_max:
                self.push_max_heap_element(num, self.added_count)
            else:
                self.push_min_heap_element(num, self.added_count)
        else:
            self.push_max_heap_element(num, self.added_count)
        self.elems[self.added_count] = num
        self.added_count += 1
        self.rebalance()

    def findMedian(self) -> float:
        if self.max_heap_count == self.min_heap_count:
            v_max, _ = self.peek_max_heap()
            v_min, _ = self.peek_min_heap()
            return (v_max + v_min) / 2
        else:
            v, _ = self.peek_max_heap()
            return v

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# leetcode submit region end(Prohibit modification and deletion)
