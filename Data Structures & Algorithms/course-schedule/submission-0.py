from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        dependents = [[] for _ in range(numCourses)]

        queue = deque()
        for course, prerequisite in prerequisites:
            dependents[prerequisite].append(course)
            indegree[course] += 1
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        
        finished = 0
        while queue:
            course = queue.popleft()
            finished += 1

            for dependent in dependents[course]:
                
                indegree[dependent] -= 1
                if indegree[dependent] == 0:
                    queue.append(dependent)
        return finished == numCourses
            