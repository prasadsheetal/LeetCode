class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        distinct = list(set(nums))
        distinct.sort(reverse=True)
        if len(distinct) >= 3:
            return distinct[2]

        return distinct[0]
        