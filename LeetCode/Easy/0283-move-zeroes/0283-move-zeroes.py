class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        lastNonZeroFoundAt = 0
        cur = 0

        while cur < len(nums):
            if nums[cur] != 0:
                nums[lastNonZeroFoundAt], nums[cur] = nums[cur], nums[lastNonZeroFoundAt]
                lastNonZeroFoundAt += 1
            cur += 1