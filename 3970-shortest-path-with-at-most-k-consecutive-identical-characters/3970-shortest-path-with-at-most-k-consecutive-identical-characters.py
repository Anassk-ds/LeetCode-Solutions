
import heapq

class Solution:
    def shortestPath(self, n: int, edges: list[list[int]], labels: str, k: int) -> int:
        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))

        inf = float('inf')
        dist = [[inf] * (k + 1) for _ in range(n)]

        dist[0][1] = 0
        heap = [(0, 0, 1)]

        while heap:
            cost, u, count = heapq.heappop(heap)

            if cost != dist[u][count]:
                continue

            if u == n - 1:
                return cost

            for v, w in graph[u]:
                next_count = count + 1 if labels[u] == labels[v] else 1

                if next_count > k:
                    continue

                next_cost = cost + w

                if next_cost < dist[v][next_count]:
                    dist[v][next_count] = next_cost
                    heapq.heappush(heap, (next_cost, v, next_count))

        return -1
