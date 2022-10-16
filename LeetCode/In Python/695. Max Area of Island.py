from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def dfs(r, c):
            if (r, c) not in stack and grid[r][c] == 1:
                stack.add((r, c))
                counter[0] += 1
                if r > 0: dfs(r - 1, c)
                if r + 1 < R: dfs(r + 1, c)
                if c > 0: dfs(r, c - 1)
                if c + 1 < C: dfs(r, c + 1)

        m = 0
        stack = set()  # accessing set is very fast (Sets are implemented using hash tables)
        R, C = len(grid), len(grid[0])
        for r in range(R):
            for c in range(C):
                if (r, c) not in stack and grid[r][c] == 1:
                    counter = [0]
                    dfs(r, c)
                    if counter[0] > m:
                        m = counter[0]
        return m