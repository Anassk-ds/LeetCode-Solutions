class Solution:
    def sumOfSquares(self, nums):
        n = len(nums)
        total = 0

        for i, num in enumerate(nums, start=1):
            if n % i == 0:
                total += num * num

        return total
