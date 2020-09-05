# https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        
        indegrees = [0] * numCourses
        visited = []
        graph = {}
        for item in prerequisites:
            course, prerequisite = item
            outdegrees[prerequisite] += 1 
            indegrees[course] += 1
            
            if prerequisite not in graph:
                graph[prerequisite] = [course] 
            else:
                graph[prerequisite].append(course)
                
        queue = [i for i in range(numCourses) if indegrees[i] == 0]
        order_course = []
        while queue:
            cur_course = queue.pop(0)
            order_course.append(cur_course)
            
            if cur_course in graph:
                neighs = graph[cur_course]
                for neigh in neighs:
                    indegrees[neigh] -= 1
                    if indegrees[neigh] == 0:
                        queue.append(neigh)
            if len(order_course) == numCourses:
                return True
        return False
