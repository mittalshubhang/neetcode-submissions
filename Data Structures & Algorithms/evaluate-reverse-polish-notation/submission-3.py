class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for char in tokens:
            if char.isdigit() or (char.startswith("-") and char[1:].isdigit()):
                stack.append(int(char))
            else:
                b = stack.pop()
                a = stack.pop()
                if char == "+":
                    stack.append(a+b)
                elif char == "-":
                    stack.append(a-b)
                elif char == "*":
                    stack.append(a*b)
                elif char == "/":
                    stack.append(int(a/b))
        
        return stack[-1]
        