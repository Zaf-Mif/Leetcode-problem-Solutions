# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def dfs(node , visited):

            if node == destination:
                return True

            visited.add(node) # adding the node into visited 

            for nb in graph[node]:
                if nb not in visited : # checking if it's visited
                    found = dfs(nb , visited)

                    if found :
                        return True

            return False

        # change edge list to adjacency list
        graph = defaultdict(list)
        for u , v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # visited to track the visit element 
        visited = set()

        # calling dfs with source 
        return  dfs(source , visited)