class Solution:
    
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        # Initution: Use DFS to loop through each possible room starting from room 0
        # visited = set()
        # n = len(rooms)
        # stack = [0]
        # while stack:
        #     room = stack.pop()
        #     for key in rooms[room]:
        #         if key not in visited:
        #             stack.append(key)
        #     visited.add(room)
        # return len(visited) == n

        visited = set()
        def dfs(room):
            visited.add(room)
            for key in rooms[room]:
                if key not in visited:
                    dfs(key)
        dfs(0)
        return len(visited) == len(rooms)