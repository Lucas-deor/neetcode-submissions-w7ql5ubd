class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashAux = {}
        for num in nums:
            if num not in hashAux:
                hashAux[num] = 1
            else:
                hashAux[num] += 1
                return True
        return False
                