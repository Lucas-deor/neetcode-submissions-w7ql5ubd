class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        L = 0
        sumValues = 0

        for R in range(len(arr)):
            sumValues += arr[R]

            if R - L + 1 == k:
                if sumValues >= threshold * k:
                    res += 1
                sumValues -= arr[L]
                L += 1
        
        return res