class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        import math

        stack = []

        for i in range(len(tokens)):
            if tokens[i] == "+":
                first_el = stack.pop()
                second_el = stack.pop()
                stackSum = first_el + second_el
                stack.append(stackSum)
            elif tokens[i] == "*":
                first_el = stack.pop()
                second_el = stack.pop()

                stackMult = first_el * second_el
                stack.append(stackMult)
            elif tokens[i] == "-":
                first_el = stack.pop()
                second_el = stack.pop()

                stackSub = second_el - first_el
                stack.append(stackSub)
            elif tokens[i] == "/":
                first_el = stack.pop()
                second_el = stack.pop()

                stackDiv = math.trunc(second_el / first_el)
                stack.append(stackDiv)
            else:
                stack.append(int(tokens[i]))
        
        return stack[0]

        