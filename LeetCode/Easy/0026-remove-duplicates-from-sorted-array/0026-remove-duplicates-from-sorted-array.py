class Solution:
    # My solution
    def removeDuplicates(self, nums: List[int]) -> int:
        cur = 0
        for num in nums:
            if num != nums[cur]:
                cur += 1
                nums[cur] = num
        return cur + 1
        