
class Solution:
    def maxAlternatingSum(self, nums):
        squares = sorted((num * num for num in nums), reverse=True)
        half = (len(squares) + 1) // 2

        return sum(squares[:half]) - sum(squares[half:])
