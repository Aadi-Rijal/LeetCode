class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        lock = 0
        for num in nums:
            if num == nums[0]:
                count += 1
            else:
                if lock == 0:
                    other_element = num
                    lock = 1
                count -=1
        return nums[0] if count > 0 else other_element
        