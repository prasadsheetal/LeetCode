class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count=0
        zeroes=0
        for num in nums:
            if num ==0:
                zeroes+=1
                count += zeroes
            else:
                zeroes=0
        return count