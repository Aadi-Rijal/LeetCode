class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        current_sum = 0
        max_score = 0
        seen = set()
        for right in range(len(nums)):
            while nums[right] in seen:
                current_sum -= nums[left]
                seen.remove(nums[left])
                left += 1
            seen.add(nums[right])
            current_sum += nums[right]
            max_score = max(max_score, current_sum)
        return max_score
