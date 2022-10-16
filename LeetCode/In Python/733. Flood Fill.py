from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color: return image

        R, C = len(image), len(image[0])
        init_color = image[sr][sc]

        def dfs(r, c):
            if image[r][c] == init_color:
                image[r][c] = color
                if r > 0:
                    dfs(r - 1, c)
                if r + 1 < R:
                    dfs(r + 1, c)
                if c > 0:
                    dfs(r, c - 1)
                if c + 1 < C:
                    dfs(r, c + 1)

        dfs(sr, sc)
        return image