class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0
        for r in range(len(nums)):
            if num[r]:
                num[l], num[r] = num[r], num[l]
                l += 1