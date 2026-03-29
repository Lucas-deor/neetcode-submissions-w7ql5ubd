class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # [["a", 1], ["j", 2]]
        stack = []

        for i in range(len(s)):
            if stack and s[i] == stack[-1][0]:
                stack[-1][1] += 1
            else:
                stack.append([s[i], 1])

            if stack[-1][1] == k:
                stack.pop()

        return "".join(char * count for char, count in stack)
                
