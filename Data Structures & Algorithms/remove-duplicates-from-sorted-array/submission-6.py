class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        rmvSet = sorted(set(nums))
        k = len(rmvSet)
        nums[:k] = rmvSet
        return k