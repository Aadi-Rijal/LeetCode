class Solution:
    def maxSum(self, nums: List[int]) -> int:
        positiveSet= set([num for num in nums if num > 0])
        return max(nums) if len(positiveSet) == 0 else sum(positiveSet)
        