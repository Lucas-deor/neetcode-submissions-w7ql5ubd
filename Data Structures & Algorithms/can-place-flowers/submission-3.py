class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if i == 0 and len(flowerbed) == 1 and flowerbed[i] == 0:
                flowerbed[i] = 1
                n -= 1
                continue

            if i == 0 and len(flowerbed) > 1 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1
                continue

            if i == (len(flowerbed) - 1) and flowerbed[i] == 0 and flowerbed[i - 1] == 0:
                flowerbed[i] = 1
                n -= 1
                continue

            if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1
                continue
        
        if n > 0:
            return False
        else:
            return True

