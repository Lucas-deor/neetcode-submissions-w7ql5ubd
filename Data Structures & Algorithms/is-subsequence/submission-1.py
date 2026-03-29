class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        k = 0 

        for i in range(len(t)):
            if not s:
                return True

            if t[i] == s[k]:
                k += 1
            if k == len(s):
                return True

        return False


            


        