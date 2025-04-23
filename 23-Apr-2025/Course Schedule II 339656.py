# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

# By using DFS
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        color = [0] *numCourses
        order = []

        for course , pre in prerequisites:
            graph[pre].append(course)
        
        def topsort(node):
            if color[node] == 1:
                return False
            if color[node] == 2:
                return True
            
            color[node] = 1

            for nb in graph[node]:
                if not topsort(nb):
                    return False
            
            color[node] = 2
            order.append(node)
            return True
        
        for course in range(numCourses):
            if color[course] == 0:
                if not topsort(course):
                    return []

        return order[::-1]