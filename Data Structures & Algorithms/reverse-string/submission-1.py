class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        
        for r in range(len(s) - 1, -1, -1):
            if l >= len(s) // 2 or r == l:
                return s
            
            s[l], s[r] = s[r], s[l]
            l += 1
        return s