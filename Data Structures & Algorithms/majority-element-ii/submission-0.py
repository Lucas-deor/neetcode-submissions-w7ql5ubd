class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        hashCounter = {}
        res = set()

        for i in range(n):
            if nums[i] in hashCounter:
                hashCounter[nums[i]] += 1
            else:
                hashCounter[nums[i]] = 1
        
        for i in range(n):
            if hashCounter[nums[i]] > n / 3:
                res.add(nums[i])

        return list(res)