class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_copy = []
        for i, num in enumerate(nums):
            nums_copy.append([num, i])

        nums_copy.sort()

        l, r = 0, len(nums) - 1

        while l < r:
            curr = nums_copy[l][0] + nums_copy[r][0]

            if curr < target:
                l += 1
            elif curr > target:
                r -= 1
            else:
                return [min(nums_copy[l][1], nums_copy[r][1]), max(nums_copy[l][1], nums_copy[r][1])]
        
        return []