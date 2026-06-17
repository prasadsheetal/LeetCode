class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        left = 0
        curr_sum = 0
        max_sum = 0
        freq = {}

        for right in range(len(nums)):
            curr_sum += nums[right]
            freq[nums[right]] = freq.get(nums[right], 0 ) + 1

            if right - left + 1 > k:
                curr_sum -= nums[left]
                freq[nums[left]] -= 1

                if freq[nums[left]] == 0:
                    del freq[nums[left]]

                left += 1

            if right - left + 1 == k:
                if len(freq) == k:
                    max_sum = max(max_sum, curr_sum)

        return max_sum
        