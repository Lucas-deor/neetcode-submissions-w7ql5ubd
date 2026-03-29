class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        opening_stack = []
        
        for c in s:
            if c in hash_map:
                if opening_stack and opening_stack[-1] == hash_map[c]:
                    opening_stack.pop()
                else:
                    return False
            else:
                opening_stack.append(c)
        
        return True if not opening_stack else False