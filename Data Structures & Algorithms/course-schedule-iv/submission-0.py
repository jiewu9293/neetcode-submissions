from collections import deque
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        all_prereqs = [set() for _ in range(numCourses)]
        next_courses = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for prerequisite,course in prerequisites:
            next_courses[prerequisite].append(course)
            indegree[course] += 1
        queue = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        while queue:
            course = queue.popleft()

            for next_course in next_courses[course]:
                all_prereqs[next_course].add(course)
                all_prereqs[next_course].update(all_prereqs[course])

                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)
        answer = []                     
        for prereq,course in queries:
            is_prereq = prereq in all_prereqs[course]
            answer.append(is_prereq)
        return answer
