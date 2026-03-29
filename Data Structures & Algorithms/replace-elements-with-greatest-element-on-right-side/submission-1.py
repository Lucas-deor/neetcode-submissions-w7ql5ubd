class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)

        for i in range(length):
            greatest = 0
            for j in range(i + 1, length):
                if arr[j] >= greatest:
                    greatest = arr[j]
                    arr[i] = greatest

            if i + 1 == length:
                arr[i] = -1

        return arr