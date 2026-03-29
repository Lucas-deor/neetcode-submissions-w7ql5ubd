class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        rem_s = s.strip()
        print(rem_s)
        count = 0

        for i in range(len(rem_s) - 1, -1, -1):
            if rem_s[i] == ' ':
                return count
            else:
                count += 1
        
        return count