class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        nums.sort()


        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums)):

                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                l, r = j + 1, len(nums) - 1
                while l < r:
                    diff = target - nums[i] - nums[j]
                    sumPointers = nums[l] + nums[r]

                    if sumPointers < diff:
                        l += 1
                    elif sumPointers > diff:
                        r -= 1
                    else:
                        output.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1

                        while nums[l] == nums[l - 1] and l < r:
                            l += 1
        
        return output
