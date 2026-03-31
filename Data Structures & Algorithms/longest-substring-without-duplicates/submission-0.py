class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        output = 0
        L = 0
        hashset = set()

        for R in range(len(s)):
            if s[R] in hashset:
                while s[R] in hashset:
                    hashset.remove(s[L])
                    L += 1
            
            hashset.add(s[R])

            output = max(output, R - L + 1)
        return output
