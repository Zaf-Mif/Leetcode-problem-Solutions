# Problem: Longest Increasing Path in a Matrix - https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m , n= len(matrix) ,len(matrix[0])

        # the padines
        mat = [[0]*(n+2) for _ in range(m+2)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                mat[i][j] = matrix[i-1][j-1]

        # directions and outdegree
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        outdegree =  [[0]*(n+2) for _ in range(m+2)]

        # for outdegree
        for i in range(1,m+1):
            for j in range(1,n+1):
                for x , y in directions:
                    dx = i + x
                    dy = j + y
                    if mat[i][j] < mat[dx][dy]:
                        outdegree[i][j] += 1

        leaves = deque()
        for i in range(1,m+1):
            for j in range(1,n+1):
                if outdegree[i][j] == 0:
                    leaves.append((i,j))

        ans = 0
        while leaves:
            ans += 1

            new_leaves =deque()
            for i , j  in leaves :
                for dx,dy in directions:
                    x = dx + i
                    y = dy + j
                    if mat[x][y] < mat[i][j]:
                        outdegree[x][y] -= 1
                        if outdegree[x][y] == 0:
                            new_leaves.append((x,y))
            
            leaves = new_leaves

        return ans