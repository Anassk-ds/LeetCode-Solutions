
class Solution:
    def sumCounts(self, nums):
        MOD = 10**9 + 7
        n = len(nums)

        tree_sum = [0] * (4 * n)
        tree_sq = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def apply(node, left, right, value):
            length = right - left + 1
            tree_sq[node] = (
                tree_sq[node]
                + 2 * value * tree_sum[node]
                + value * value * length
            ) % MOD

            tree_sum[node] = (
                tree_sum[node] + value * length
            ) % MOD

            lazy[node] += value

        def push(node, left, right):
            if lazy[node] == 0 or left == right:
                return

            mid = (left + right) // 2
            value = lazy[node]

            apply(node * 2, left, mid, value)
            apply(node * 2 + 1, mid + 1, right, value)

            lazy[node] = 0

        def update(node, left, right, ql, qr):
            if ql <= left and right <= qr:
                apply(node, left, right, 1)
                return

            push(node, left, right)
            mid = (left + right) // 2

            if ql <= mid:
                update(node * 2, left, mid, ql, qr)

            if qr > mid:
                update(node * 2 + 1, mid + 1, right, ql, qr)

            tree_sum[node] = (
                tree_sum[node * 2] + tree_sum[node * 2 + 1]
            ) % MOD

            tree_sq[node] = (
                tree_sq[node * 2] + tree_sq[node * 2 + 1]
            ) % MOD

        last_seen = {}
        answer = 0

        for i, num in enumerate(nums):
            left = last_seen.get(num, -1) + 1
            update(1, 0, n - 1, left, i)

            answer = (answer + tree_sq[1]) % MOD
            last_seen[num] = i

        return answer
