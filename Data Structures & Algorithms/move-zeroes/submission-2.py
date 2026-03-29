class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for i in range(1, len(nums)):
            if nums[l] != 0:
                l += 1

            if nums[l] == 0 and nums[i] != 0:
                left_numb = nums[l]
                nums[l] = nums[i]
                nums[i] = left_numb
                l += 1
        