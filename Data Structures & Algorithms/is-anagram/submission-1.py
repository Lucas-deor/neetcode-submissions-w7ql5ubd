class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_sorted = sorted(s)
        t_sorted = sorted(t)

        if len(s) != len(t):
            return False
        
        if s_sorted != t_sorted:
            return False
        
        return True
        
