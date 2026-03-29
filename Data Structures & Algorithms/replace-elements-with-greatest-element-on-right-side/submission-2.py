class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l = 0

        while l < len(arr):
            biggest_aux = 0

            for r in range(l + 1, len(arr)):
                if arr[r] > biggest_aux:
                    biggest_aux = arr[r]
            arr[l] = biggest_aux
            l += 1
        
        arr[-1] = -1
        return arr
        
