class Solution:
    def maxArea(self, heights: List[int]) -> int:

        max_area = 0

        def amountWater(base, height):
            return base * height

        l = 0

        while l < len(heights) - 1:
            r = l + 1
            while r < len(heights):
                h = min(heights[l], heights[r])
                aux = amountWater(r - l, h)
                if aux > max_area:
                    max_area = aux

                r += 1
            l += 1

        return max_area
        

