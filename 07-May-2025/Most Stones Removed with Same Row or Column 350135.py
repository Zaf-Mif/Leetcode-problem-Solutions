# Problem: Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class UnionFind:
    def __init__ (self,n):
        self.parent = [i for i in range(n)]
        self.count = n
        self.size = [1] *n
    
    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)

        if parent_x == parent_y:
            return
        
        if parent_x != parent_y:
            if self.size[parent_x] > self.size[parent_y]:
                self.size[parent_x] += self.size[parent_y]
                self.parent[parent_y] = parent_x
            else:
                self.size[parent_y] += self.size[parent_x]
                self.parent[parent_x] = parent_y
            
        self.count -= 1        

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        N = len(stones)
        uf = UnionFind(N)

        for i in range(N):
            for j in range(i+1 , N):
                if stones[i][0] == stones[j][0] or stones[j][1] == stones[i][1]:
                    uf.union(i,j)
        
        return N - uf.count