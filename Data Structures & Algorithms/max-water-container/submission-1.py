class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        l, r = 0, len(heights) - 1

        while l < r:
            h = min(heights[l], heights[r])
            aux = (r - l) * h

            if aux > max_area:
                max_area = aux
            
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_area
        

