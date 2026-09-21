class Solution:
    def resultArray(self, nums, k):
        dp = [0] * k
        result = [0] * k

        for num in nums:
            remainder = num % k
            new_dp = [0] * k

            # Start a new subarray with the current element
            new_dp[remainder] += 1

            # Extend previous subarrays
            for r in range(k):
                if dp[r] > 0:
                    new_remainder = (r * remainder) % k
                    new_dp[new_remainder] += dp[r]

            # Add subarrays ending at the current position
            for r in range(k):
                result[r] += new_dp[r]

            dp = new_dp

        return result
