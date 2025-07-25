class Solution:
    def maxSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        set_unique_nums = set()
        max_negative = float(-inf)
        result = 0
        for num in nums:
            if num > 0:
                set_unique_nums.add(num)
            else:
                max_negative = max(num, max_negative)
        for num in set_unique_nums:
            result += num
        if result == 0:
            result += max_negative

        return result
        