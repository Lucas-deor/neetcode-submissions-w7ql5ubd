class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        while l < len(nums):
            for r in range(1, len(nums)):
                if nums[l] > nums[r] and l < r:
                    nums[l], nums[r] = nums[r], nums[l]
                    print(nums)
            l += 1        


        