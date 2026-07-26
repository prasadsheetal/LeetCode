class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for number in nums:
            index = abs(number) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]
        missing = []
        for index in range(len(nums)):
            if nums[index] > 0:
                missing.append(index+1)

        return missing