class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashmap = {}
        i = 0

        while i < len(s):
            if s[i] in hashmap and t[i] != hashmap[s[i]]:
                return False

            if t[i] in hashmap.values() and s[i] not in hashmap:
                return False
            
            hashmap[s[i]] = t[i]
            i += 1
        return True