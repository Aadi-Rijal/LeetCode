class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0,1]
        
        for i in range(len(nums)):
            req = target - nums[i]
            if req in nums[i+1:]:
                return [i , nums.index(req,i+1)]