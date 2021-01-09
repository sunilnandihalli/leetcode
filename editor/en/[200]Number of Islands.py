# Given a 2d grid map of '1's (land) and '0's (water), count the number of islan
# ds. An island is surrounded by water and is formed by connecting adjacent lands 
# horizontally or vertically. You may assume all four edges of the grid are all su
# rrounded by water. 
# 
#  Example 1: 
# 
#  
# Input:
# 11110
# 11010
# 11000
# 00000
# 
# Output: 1
#  
# 
#  Example 2: 
# 
#  
# Input:
# 11000
# 11000
# 00100
# 00011
# 
# Output: 3
#  Related Topics Depth-first Search Breadth-first Search Union Find
from typing import List


def test():
    s = Solution()
    m = 2
    n = 2
    actual = s.numIslands([['1'] * n] * m)
    expected = 1
    print(actual, expected)
    assert actual == expected


# leetcode submit region begin(Prohibit modification and deletion)
def neighbors(cur, land):
    i, j = cur
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ni = i + di
        nj = j + dj
        if (ni, nj) in land:
            yield ni, nj


def display(x, m, n):
    print('_' * n)
    print('\n'.join([''.join(['#' if (i, j) in x else '.' for i in range(n)]) for j in range(m)]))
    print('_' * n)


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0]) if m > 0 else 0
        land = set([(i, j) for i, row in enumerate(grid) for j, v in enumerate(row) if v == '1'])
        num_islands = 0

        while len(land) > 0:
            num_islands += 1
            island_start = land.pop()
            front = set([island_start])
            visited = set([island_start])
            island = set()
            while len(front) > 0:
                x = front.pop()
                island.add(x)
                neis = list(neighbors(x, land))
                for nei in neis:
                    if nei not in visited:
                        front.add(nei)
                        visited.add(nei)
                        land.remove(nei)
        return num_islands

        # leetcode submit region end(Prohibit modification and deletion)
