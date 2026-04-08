class Solution:
    def countElements(self, arr: List[int]) -> int:
        output = 0
        ctr = Counter(arr)

        for i in range(len(arr)):
            if arr[i] + 1 in ctr:
                output += 1
        
        return output