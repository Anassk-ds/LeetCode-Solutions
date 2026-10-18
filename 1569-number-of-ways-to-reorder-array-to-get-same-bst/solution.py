
class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # Precompute Pascal's triangle:
        # comb[i][j] = number of ways to choose j elements from i.
        comb = [[0] * n for _ in range(n)]

        for i in range(n):
            comb[i][0] = 1
            for j in range(1, i + 1):
                if j == i:
                    comb[i][j] = 1
                else:
                    comb[i][j] = (
                        comb[i - 1][j - 1] + comb[i - 1][j]
                    ) % MOD

        def count_ways(arr: list[int]) -> int:
            if len(arr) <= 2:
                return 1

            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]

            left_ways = count_ways(left)
            right_ways = count_ways(right)

            # Interleave left and right subtree elements while
            # preserving the relative order within each subtree.
            interleavings = comb[len(left) + len(right)][len(left)]

            return (
                interleavings * left_ways * right_ways
            ) % MOD

        # Exclude the original ordering itself.
        return (count_ways(nums) - 1) % MOD
