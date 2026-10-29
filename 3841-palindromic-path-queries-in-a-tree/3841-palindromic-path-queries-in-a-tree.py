
class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        parent = [-1] * n
        depth = [0] * n
        order = [0]
        parent[0] = 0

        for u in order:
            for v in graph[u]:
                if v != parent[u]:
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    order.append(v)

        size = [1] * n
        heavy = [-1] * n

        for u in reversed(order):
            largest = 0
            for v in graph[u]:
                if parent[v] == u:
                    size[u] += size[v]
                    if size[v] > largest:
                        largest = size[v]
                        heavy[u] = v

        head = [0] * n
        pos = [0] * n
        timer = 0
        chains = [(0, 0)]

        while chains:
            u, h = chains.pop()

            while u != -1:
                head[u] = h
                pos[u] = timer
                timer += 1

                for v in graph[u]:
                    if parent[v] == u and v != heavy[u]:
                        chains.append((v, v))

                u = heavy[u]

        seg = [0] * (2 * n)

        for u in range(n):
            seg[n + pos[u]] = 1 << (ord(s[u]) - ord('a'))

        for i in range(n - 1, 0, -1):
            seg[i] = seg[i * 2] ^ seg[i * 2 + 1]

        def update(index: int, value: int) -> None:
            index += n
            seg[index] = value
            index //= 2

            while index:
                seg[index] = seg[index * 2] ^ seg[index * 2 + 1]
                index //= 2

        def range_xor(left: int, right: int) -> int:
            result = 0
            left += n
            right += n + 1

            while left < right:
                if left & 1:
                    result ^= seg[left]
                    left += 1

                if right & 1:
                    right -= 1
                    result ^= seg[right]

                left //= 2
                right //= 2

            return result

        def path_xor(u: int, v: int) -> int:
            result = 0

            while head[u] != head[v]:
                if depth[head[u]] < depth[head[v]]:
                    u, v = v, u

                result ^= range_xor(pos[head[u]], pos[u])
                u = parent[head[u]]

            if depth[u] > depth[v]:
                u, v = v, u

            result ^= range_xor(pos[u], pos[v])
            return result

        chars = list(s)
        answer = []

        for query in queries:
            parts = query.split()
            u = int(parts[1])

            if parts[0] == "update":
                c = parts[2]
                chars[u] = c
                update(pos[u], 1 << (ord(c) - ord('a')))
            else:
                v = int(parts[2])
                mask = path_xor(u, v)
                answer.append(mask & (mask - 1) == 0)

        return answer
