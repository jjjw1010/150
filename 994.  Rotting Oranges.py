from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Initution use BFS
        # First find rotten oranges and append to queue and find number of fresh oranges
        # BFS each rotten oranges and append its 4 directionally adjacent oranges 
        # Increment time at each level of BFS when there exists a fresh orange
        dq = deque()
        m = len(grid)
        n = len(grid[0])
        fresh = 0
        rotten = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    dq.append([i, j])
                if grid[i][j] == 1:
                    fresh += 1
        time = 0
        if fresh == 0: return time
        while dq:
            if fresh != 0: time += 1
            for _ in range(len(dq)):
                orange = dq.popleft()
                ox, oy = orange[0], orange[1]
                for x, y in [[0,1],[1,0],[-1,0],[0,-1]]:
                    new_x, new_y = x + ox, y + oy
                    if new_x < m and new_x >= 0 and new_y < n and new_y >= 0:
                        if grid[new_x][new_y] == 1:
                            fresh -= 1
                            grid[new_x][new_y] = 2
                            dq.append([new_x, new_y])
        return time if fresh == 0 else -1