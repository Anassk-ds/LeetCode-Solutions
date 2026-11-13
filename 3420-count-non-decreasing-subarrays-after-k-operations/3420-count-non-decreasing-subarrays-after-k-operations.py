class Solution:
    def countNonDecreasingSubarrays(self, nums: list[int], k: int) -> int:
        n = len(nums)

        nxt = [n] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()

            if stack:
                nxt[i] = stack[-1]

            stack.append(i)

        chain_sum = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            chain_sum[i] = (
                nums[i] * (nxt[i] - i) + chain_sum[nxt[i]]
            )

        levels = n.bit_length()
        up = [nxt]

        for j in range(1, levels):
            prev = up[-1]
            curr = [n] * n

            for i in range(n):
                curr[i] = prev[prev[i]] if prev[i] < n else n

            up.append(curr)

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        def get_cost(left, right):
            pos = left

            for j in range(levels - 1, -1, -1):
                nxt_pos = up[j][pos]

                if nxt_pos <= right:
                    pos = nxt_pos

            maximum_sum = (
                chain_sum[left]
                - chain_sum[pos]
                + nums[pos] * (right - pos + 1)
            )

            return maximum_sum - (prefix[right + 1] - prefix[left])

        ans = 0
        left = 0

        for right in range(n):
            while get_cost(left, right) > k:
                left += 1

            ans += right - left + 1

        return ans