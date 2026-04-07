class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        crt = Counter(nums)
        res = 0

        for i in range(len(nums)):
            if crt[nums[i]] == 1:
                res = max(res, nums[i])
        
        return res if res > 0 else -1


