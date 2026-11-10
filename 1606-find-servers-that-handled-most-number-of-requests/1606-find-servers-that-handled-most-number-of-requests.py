import heapq
from sortedcontainers import SortedList

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        available = SortedList(range(k))
        busy = []
        counts = [0] * k

        for i, (start, duration) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= start:
                _, server = heapq.heappop(busy)
                available.add(server)

            if not available:
                continue

            server = available.bisect_left(i % k)

            if server == len(available):
                server = 0

            server = available.pop(server)

            counts[server] += 1
            heapq.heappush(busy, (start + duration, server))

        maximum = max(counts)

        return [i for i in range(k) if counts[i] == maximum]