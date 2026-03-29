class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    for l in range(k + 1, len(nums)):
                        totalSum = nums[i] + nums[j] + nums[k] + nums[l]

                        if totalSum == target:
                            subarray = [nums[i], nums[j], nums[k], nums[l]]
                            subarray.sort()

                            if subarray not in output:
                                output.append(subarray)
        
        return output