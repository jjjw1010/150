class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        inDegree = [0 for _ in range(numCourses)]
        
        # a <- b for each prereq
        for a, b in prerequisites:
            graph[b].append(a)
            inDegree[a] += 1
        
        # Find Courses with no PreReq
        dq = collections.deque([])
        for i in range(numCourses):
            if inDegree[i] == 0:
                dq.append(i)
        
        tookCourse = 0

        # Iterate until you can't find courses with no prereq fulfilled
        while dq:
            course = dq.popleft()
            tookCourse += 1

            for nextCourse in graph[course]:
                inDegree[nextCourse] -= 1

                if inDegree[nextCourse] == 0:
                    dq.append(nextCourse)
        return tookCourse == numCourses        
