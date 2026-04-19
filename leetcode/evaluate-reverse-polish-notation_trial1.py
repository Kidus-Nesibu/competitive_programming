class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for i in range(len(tokens)):

            if tokens[i] == '+':
                num1 = stack.pop()
                num2 = stack.pop()
                val = num2 + num1
                stack.append(int(val))
            elif tokens[i] == '-':
                num1 = stack.pop()
                num2 = stack.pop()
                val = num2 - num1
                stack.append(int(val))
            elif tokens[i] == '*':
                num1 = stack.pop()
                num2 = stack.pop()
                val = num2 * num1
                stack.append(int(val))
            elif tokens[i] == '/':
                num1 = stack.pop()
                num2 = stack.pop()
                val = num2 / num1
                stack.append(int(val))
            else:
                val = tokens[i]
                stack.append(int(val))

        return stack[0]