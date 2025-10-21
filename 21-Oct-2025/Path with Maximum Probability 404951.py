# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = [[] for _ in range(n)]
        for (u, v), p in zip(edges, succProb):
            graph[u].append((v, p))
            graph[v].append((u, p))
        dist = [0.0] * n
        dist[start_node] = 1.0
        heap = [(-1.0, start_node)]
        while heap:
            cur_prob, node = heapq.heappop(heap)
            cur_prob = -cur_prob  

            if node == end_node:
                return cur_prob

            for nei, prob in graph[node]:
                new_prob = cur_prob * prob
                if new_prob > dist[nei]:
                    dist[nei] = new_prob
                    heapq.heappush(heap, (-new_prob, nei))

        return 0.0