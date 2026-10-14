
class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""

        nines, remainder = divmod(sum, 9)
        result = "9" * nines

        if nines < num and remainder > 0:
            result += str(remainder)

        result += "0" * (num - len(result))
        return result
