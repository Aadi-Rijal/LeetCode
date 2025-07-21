class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        right = 1
        while right < len(nums):
            if nums[left] == 0:
                if nums[right] != 0:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
            else:
                left += 1
            right += 1

        