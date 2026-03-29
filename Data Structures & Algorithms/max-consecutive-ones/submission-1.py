class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consec = count = 0

        for num in nums:
            if num == 0:
                max_consec = max(max_consec, count)
                count = 0
            else:
                count += 1
        
        return max(count, max_consec)



