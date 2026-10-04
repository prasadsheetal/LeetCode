class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num,0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in freq.items() :
            buckets[count].append(num)

        ans = []

        for count in range(len(buckets) - 1, 0, -1):
            for num in buckets[count]:
                ans.append(num)

                if len(ans) == k:
                    return ans
