class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        l = 0
        while l < len(nums):
            for r in range(len(nums)):
                if nums[l] < nums[r]:
                    nums[l], nums[r] = nums[r], nums[l]
            
            l += 1
        return nums