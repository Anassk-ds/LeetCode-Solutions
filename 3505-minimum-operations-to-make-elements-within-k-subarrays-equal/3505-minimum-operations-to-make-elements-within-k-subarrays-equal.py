
class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        n = len(nums)
        values = sorted(set(nums))
        size = len(values)
        index = {v: i for i, v in enumerate(values)}

        count_bit = [0] * (size + 1)
        sum_bit = [0] * (size + 1)

        def update(bit, i, delta):
            i += 1
            while i <= size:
                bit[i] += delta
                i += i & -i

        def query(bit, i):
            result = 0
            while i > 0:
                result += bit[i]
                i -= i & -i
            return result

        def get_median(rank):
            i = 0
            step = 1 << (size.bit_length() - 1)

            while step:
                nxt = i + step
                if nxt <= size and count_bit[nxt] < rank:
                    i = nxt
                    rank -= count_bit[nxt]
                step >>= 1

            return i

        def add(value, delta):
            idx = index[value]
            update(count_bit, idx, delta)
            update(sum_bit, idx, value * delta)

        costs = []
        window_sum = 0

        for v in nums[:x]:
            add(v, 1)
            window_sum += v

        for start in range(n - x + 1):
            median_idx = get_median((x + 1) // 2)
            median = values[median_idx]

            left_count = query(count_bit, median_idx)
            left_sum = query(sum_bit, median_idx)

            count_le = query(count_bit, median_idx + 1)
            sum_le = query(sum_bit, median_idx + 1)

            right_count = x - count_le
            right_sum = window_sum - sum_le

            cost = (
                median * left_count - left_sum
                + right_sum - median * right_count
            )

            costs.append(cost)

            if start + x < n:
                outgoing = nums[start]
                incoming = nums[start + x]

                add(outgoing, -1)
                add(incoming, 1)

                window_sum += incoming - outgoing

        inf = float('inf')
        prev = [0] * (n + 1)

        for _ in range(k):
            curr = [inf] * (n + 1)

            for i in range(1, n + 1):
                curr[i] = curr[i - 1]

                if i >= x:
                    curr[i] = min(
                        curr[i],
                        prev[i - x] + costs[i - x]
                    )

            prev = curr

        return prev[n]
