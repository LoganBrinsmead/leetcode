class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visit = set()
        maxArea = 0
        rows, columns = len(grid), len(grid[0])

        def bfs(r,c):
            curArea = 0
            q = collections.deque()

            q.append((r, c))

            visit.add((r, c))
            curArea += 1

            while q:
                row, col = q.popleft()

                directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

                for dr, dc in directions:
                    r, c = dr + row, dc + col
                    if (
                        r in range(rows) and
                        c in range(columns) and
                        grid[r][c] == 1 and
                        (r, c) not in visit
                    ):
                        q.append((r,c))
                        visit.add((r,c))
                        curArea += 1
                        
            return curArea
        
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1 and (r, c) not in visit:
                    maxArea = max(bfs(r, c), maxArea)
        
        return maxArea