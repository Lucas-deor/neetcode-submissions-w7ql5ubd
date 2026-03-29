class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        T, S = 0, 0
        while T < len(t) and S < len(s):
            if s[S] == t[T]:
                S += 1
                T += 1
            else:
                S += 1
        return len(t) - T


