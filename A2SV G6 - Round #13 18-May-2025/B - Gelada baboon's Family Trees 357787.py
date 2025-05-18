# Problem: B - Gelada baboon's Family Trees - https://codeforces.com/gym/607625/problem/B

class DSU:
    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)
        self.count = n
 
    def find(self, node):
        if node == self.parent[node]:
            return node
 
        stack = []
        while node != self.parent[node]:
            stack.append(node)
            node = self.parent[node]
 
        # Path compression
        for n in stack:
            self.parent[n] = node
 
        return node
 
    def Runion(self, u, v):
        rep_u = self.find(u)
        rep_v = self.find(v)
        if rep_u == rep_v:
            return False
        if self.rank[rep_u] < self.rank[rep_v]:
            self.parent[rep_u] = rep_v
        elif self.rank[rep_v] < self.rank[rep_u]:
            self.parent[rep_v] = rep_u
        else:
            self.parent[rep_v] = rep_u
            self.rank[rep_u] += 1
        self.count -= 1
 
        return True
 
 
n = int(input())
p = list(map(int,input().split()))
dsu = DSU(n)
 
for i in range(n):
    dsu.Runion(p[i], i+1)
print(dsu.count)