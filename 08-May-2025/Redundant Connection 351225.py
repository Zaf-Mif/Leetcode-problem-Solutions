# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(1, n+1)]
        self.size = [1]*n
    
    def find(self, x):
        if self.parent[x-1] != x:
            self.parent[x-1] = self.find(self.parent[x-1])
        return self.parent[x-1]
    
    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)

        if parent_x != parent_y:
            if self.size[parent_y-1] > self.size[parent_x-1]:
                self.size[parent_y-1] += self.size[parent_x-1]
                self.parent[parent_x-1] = parent_y
            else:
                self.size[parent_x-1] += self.size[parent_y-1]
                self.parent[parent_y-1] = parent_x


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        dsu = UnionFind(N)
        arr = []
        for a,b in edges:
            pa = dsu.find(a)
            pb = dsu.find(b)
            if pa != pb:
                dsu.union(a,b)
            else:
                arr.append ([a,b])
        return arr[-1]