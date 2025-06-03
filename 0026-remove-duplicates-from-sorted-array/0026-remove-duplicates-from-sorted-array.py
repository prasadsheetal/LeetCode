class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        id=0
        for i in range (1,len(nums)):
            if nums[i]!=nums[id]:
                id +=1
                nums[id]=nums[i]
        return id+1


        