class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        my_dict = {}
        majElement = 0
        n = len(nums)

        for num in nums:
            if num in my_dict:
                my_dict[num] += 1
            else:
                my_dict[num] = 1
        
        for key, value in my_dict.items():
            if value > (n / 2):
                majElement = key
                break

        return majElement
        
