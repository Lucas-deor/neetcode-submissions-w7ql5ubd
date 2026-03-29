class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        array = [0] * len(nums)
        
        left, right = 0, len(nums) - 1
        pos = len(nums) - 1
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                array[pos] = nums[left] * nums[left]
                left += 1
                pos -= 1
            else:
                array[pos] = nums[right] * nums[right]
                right -= 1
                pos -= 1
        
        return array