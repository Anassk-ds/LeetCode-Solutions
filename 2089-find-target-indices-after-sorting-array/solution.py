
class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        return [i for i, value in enumerate(nums) if value == target]
