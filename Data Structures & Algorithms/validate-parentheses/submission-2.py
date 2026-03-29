class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching_brackets = {")": "(", "]": "[", "}": "{"}
        for char in s:
            if char in matching_brackets.values():
                stack.append(char)
            elif char in matching_brackets.keys():
                if not stack:
                    return False
                elif stack[-1] == matching_brackets[char]:
                    stack.pop()
                else: 
                    return False 
            
        return True if not stack else False