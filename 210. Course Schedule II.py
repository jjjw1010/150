class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Adjacency Matrix
        graph = collections.defaultdict(list)

        # In Degree Array
        inDegree = [0 for _ in range(numCourses)]

        for [a, b] in prerequisites:
            graph[b].append(a)
            inDegree[a] += 1

        dq = collections.deque([])
        
        for i in range(numCourses):
            if inDegree[i] == 0:
                dq.append(i)
        order = []
        count = 0
        while dq:
            course = dq.popleft()
            order.append(course)

            for nextCourse in graph[course]:
                inDegree[nextCourse] -= 1
                
                if inDegree[nextCourse] == 0:
                    dq.append(nextCourse)
            count += 1
        if count == numCourses:
            return order
        else:
            return []
        