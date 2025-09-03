# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = grid
        queue = collections.deque()
        fresh = 0
        for i in range(m):
            for j in range(n):
                if visited[i][j] == 2:
                    queue.append((i, j))
                if visited[i][j] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        if not queue:
            return -1
        
        minutes = -1
        direction = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        while queue:
            size = len(queue)
            while size > 0:
                x, y = queue.popleft()
                size -= 1
                for dx, dy in direction:
                    i, j = x + dx, y + dy
                    if 0 <= i < m and 0 <= j < n and visited[i][j] == 1:
                        visited[i][j] = 2
                        fresh -= 1
                        queue.append((i, j))
            minutes += 1
        
        if fresh == 0:
            return minutes
        return -1