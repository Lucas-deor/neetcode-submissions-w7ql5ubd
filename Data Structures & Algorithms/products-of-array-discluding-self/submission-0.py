class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        for i in range(len(nums)):
            aux_arr = list(nums)
            aux_arr.pop(i)
            cur_mult = 1

            for j in range(len(aux_arr)):
                cur_mult *= aux_arr[j]
            
            output.append(cur_mult)
        
        return output


