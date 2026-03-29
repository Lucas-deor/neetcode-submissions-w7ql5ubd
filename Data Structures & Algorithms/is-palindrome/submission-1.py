import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        res_string = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        l, r = 0, len(res_string) - 1

        print(res_string)
        
        for l in range(len(res_string)):
            if l == r:
                return True

            if res_string[l] == res_string[r]:
                r -= 1
            else:
                return False
        
        return True
