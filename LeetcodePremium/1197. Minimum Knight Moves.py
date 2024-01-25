
from collections import deque
# BFS method
def Solution(self, x, y):
    min_step = 0
    possible_moves = ((-2,-1), (-1, -2), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2))
    
    visited = set((0, 0))
    queue = deque([(0,0)])


    while queue:
        for _ in range(len(queue)):
            i, j = queue.popleft()

            if (i, j) == (x, y):
                return min_step
            
            #Continue on 8 paths
            for dx, dy in possible_moves:
                new_dx, new_dy = i + dx, j + dy

                if (new_dx, new_dy) not in visited:
                    visited.add((new_dx, new_dy))
                    queue.append((new_dx, new_dy))

        min_step += 1
    return -1

def minKnightMoves(self, x: int, y: int) -> int:

        @lru_cache(maxsize=None)
        def dfs(x, y):
            if x + y == 0:
                # base case: (0, 0)
                return 0
            elif x + y == 2:
                # base case: (1, 1), (0, 2), (2, 0)
                return 2
            else:
                return min(dfs(abs(x - 1), abs(y - 2)), dfs(abs(x - 2), abs(y - 1))) + 1

        return dfs(abs(x), abs(y))

# @cache
# Maps x,y in the parameters to the return value
# Memoization
# How would you implement this yourself
# memo = {(x,y): return value}
        memo = {}
        def dfs(x, y):
            if x + y == 0:
                # base case: (0, 0)
                return 0
            elif x + y == 2:
                # base case: (1, 1), (0, 2), (2, 0)
                return 2
            else:
                if (x,y) not in memo:
                    memo[(x,y)] = min(dfs(abs(x - 1), abs(y - 2)), dfs(abs(x - 2), abs(y - 1))) + 1
                return memo[(x,y)]
                # return min(dfs(abs(x - 1), abs(y - 2)), dfs(abs(x - 2), abs(y - 1))) + 1

        return dfs(abs(x), abs(y))