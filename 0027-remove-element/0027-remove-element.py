class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        id=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[id]=nums[i]
                id+=1
        return id
        