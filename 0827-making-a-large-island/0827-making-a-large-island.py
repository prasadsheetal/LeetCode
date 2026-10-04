class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:
        n = len(grid)
        sizes = {}
        islandId = 2

        def dfs(r, c, mark):
            if r < 0 or c < 0 or r >= n or c >= n:
                return 0

            if grid[r][c] != 1:
                return 0

            grid[r][c] = mark

            area = 1
            area += dfs(r+1,c,mark)
            area += dfs(r-1,c,mark)
            area += dfs(r,c+1,mark)
            area += dfs(r,c-1,mark)

            return area

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    sizes[islandId] = dfs(r,c,islandId)
                    islandId += 1

        best = max(sizes.values(), default =0)

        for r in range(n):
            for c in range(n):
                if grid[r][c] != 0:
                    continue

                touching = set()

                if r > 0:
                    touching.add(grid[r-1][c])
                if r + 1 < n :
                    touching.add(grid[r+1][c])
                if c > 0:
                    touching.add(grid[r][c-1])
                if c + 1 < n:
                    touching.add(grid[r][c + 1])

                area = 1

                for mark in touching:
                    if mark in sizes:
                        area += sizes[mark]
                
                best = max(best,area)

        return best




