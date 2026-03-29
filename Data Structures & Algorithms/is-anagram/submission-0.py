class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)

        for cs in s:
            s_dict[cs] += 1
        
        for ct in t:
            t_dict[ct] += 1

        if s_dict == t_dict:
            return True
        
        return False
