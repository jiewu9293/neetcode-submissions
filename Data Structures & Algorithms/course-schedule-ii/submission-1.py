from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        next_courses = [[] for _ in range(numCourses)]

        for course,prerequisite in prerequisites:
            next_courses[prerequisite].append(course)
            indegree[course] += 1
        
        queue = deque()
        order = []
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        while queue:
            course = queue.popleft()
            order.append(course)

            for next_course in next_courses[course]:
                indegree[next_course] -= 1

                if indegree[next_course] == 0:
                    queue.append(next_course)
        if len(order) == numCourses:
            return order
        else:
            return []