import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        available = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(available)

        busy = []
        ans = []

        for i, duration in enumerate(tasks):
            time = max(time if i == 0 else time, i) if busy else i

            while busy and busy[0][0] <= time:
                free_time, weight, server = heapq.heappop(busy)
                heapq.heappush(available, (weight, server))

            if not available:
                time = busy[0][0]

                while busy and busy[0][0] <= time:
                    free_time, weight, server = heapq.heappop(busy)
                    heapq.heappush(available, (weight, server))

            weight, server = heapq.heappop(available)
            ans.append(server)

            heapq.heappush(busy, (time + duration, weight, server))

        return ans