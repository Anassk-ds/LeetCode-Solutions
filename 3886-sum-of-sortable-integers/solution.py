
class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        answer = 0

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            valid = True
            prev_max = float('-inf')

            for start in range(0, n, k):
                block = nums[start:start + k]
                descents = sum(
                    block[i] > block[(i + 1) % k]
                    for i in range(k)
                )

                if descents > 1 or prev_max > min(block):
                    valid = False
                    break

                prev_max = max(block)

            if valid:
                answer += k

        return answer
