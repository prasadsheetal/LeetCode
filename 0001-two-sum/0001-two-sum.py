class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = [(nums[i], i) for i in range(len(nums))]

        pairs.sort()

        left = 0
        right = len(pairs) - 1

        while left < right:
            total = pairs[left][0] + pairs[right][0]

            if total == target:
                return [pairs[left][1], pairs[right][1]]
            elif total<target:
                left+=1
            else:
                right-=1
        return []

        
          

