# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] *numCourses
        order = []
        queue = deque()

        #  cocnstruct graph and indegree
        for course , pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        
        # check the indegree of 0 to append to the queue 
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            for nb in graph[node]:
                indegree[nb] -= 1
                print(queue)
            
                if indegree[nb] == 0:
                    queue.append(nb)

            order.append(node)
        
        return order if len(order) == numCourses else []