class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        output = 0
        L = 0

        for R in range(len(s)):
            if s[R] in hashmap:
                hashmap[s[R]] += 1
            else:
                hashmap[s[R]] = 1

            amountToReplace = (R - L + 1) - max(hashmap.values())

            if amountToReplace > k:
                while amountToReplace > k:
                    hashmap[s[L]] -= 1
                    L += 1
                    amountToReplace = (R - L + 1) - max(hashmap.values())
            
            output = max(output, R - L + 1)

        return output