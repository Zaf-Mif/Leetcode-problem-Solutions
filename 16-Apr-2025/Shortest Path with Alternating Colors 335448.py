# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        
        graph = [[[],[]] for i in range(n)]

        for a , b in redEdges:
            graph[a][0].append(b)

        for a , b in blueEdges:
            graph[a][1].append(b)

        queue = deque([(0,1), (0, 0)])
        visited = set([(0,1), (0, 0)])
        dist = 0
        ans = [-1] *n

        while queue:

            for _ in range(len(queue)):
                node , color = queue.popleft()

                if ans[node] == -1:
                    ans[node] = dist

                alter = 0
                if color == 0:
                    alter = 1
                
                # else we can assign alter to 1- color

                for nb in graph[node][alter]:
                    if (nb , alter) not in visited:
                        queue.append((nb , alter))
                        visited.add((nb , alter))

            dist += 1
        return ans





