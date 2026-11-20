class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float('inf')

        cost = [[INF] * n for _ in range(n)]

        for i in range(n):
            for length in range(2, n - i + 1):
                best = INF

                for d in range(1, length):
                    if length % d != 0:
                        continue

                    changes = 0

                    for r in range(d):
                        count = (length - 1 - r) // d + 1

                        for t in range(count // 2):
                            left = i + r + t * d
                            right = i + r + (count - 1 - t) * d

                            if s[left] != s[right]:
                                changes += 1

                    best = min(best, changes)

                cost[i][i + length - 1] = best

        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0

        for p in range(1, k + 1):
            for end in range(2 * p, n + 1):
                for start in range(2 * (p - 1), end - 1):
                    dp[p][end] = min(
                        dp[p][end],
                        dp[p - 1][start] + cost[start][end - 1]
                    )

        return dp[k][n]