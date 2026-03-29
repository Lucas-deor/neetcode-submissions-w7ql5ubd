class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        import math

        stack = []

        for i in range(len(tokens)):
            if tokens[i] == "+":
                stack.append(stack.pop() + stack.pop())
            elif tokens[i] == "*":
                stack.append(stack.pop() * stack.pop())
            elif tokens[i] == "-":
                first_el, second_el = stack.pop(), stack.pop()
                stack.append(second_el - first_el)
            elif tokens[i] == "/":
                first_el, second_el = stack.pop(), stack.pop()
                stack.append(math.trunc(second_el / first_el))
            else:
                stack.append(int(tokens[i]))
        
        return stack[0]

        