class Solution:
    def minElement(self, nums: List[int]) -> int:
        min_val=float('inf')

        for x in nums:
            digit_sum=0
            while x>0:
                digit_sum+=x%10
                x//=10
            min_val=min(min_val,digit_sum)

        return min_val

        