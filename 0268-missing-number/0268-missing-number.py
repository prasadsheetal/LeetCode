class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        totalSum = sum(nums)

        expSum = n * (n+1) // 2

        return expSum - totalSum
        