class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for i in range(len(asteroids)):
            while stack and asteroids[i] < 0 and stack[-1] > 0:
                if abs(asteroids[i]) > abs(stack[-1]):
                    stack.pop()
                elif abs(asteroids[i]) < abs(stack[-1]):
                    asteroids[i] = 0
                else:
                    asteroids[i] = 0
                    stack.pop()
            
            if asteroids[i]:
                stack.append(asteroids[i])
        
        return stack