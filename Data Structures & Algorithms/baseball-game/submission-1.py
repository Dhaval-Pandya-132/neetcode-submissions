class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = 0
        stack = []

        for operation in operations:
            if operation == "+":  
                result += stack[-1] + stack[-2]
                stack.append(stack[-1] + stack[-2])
            elif operation == "D":
                result += stack[-1]*2
                stack.append(stack[-1]*2)
            elif operation == "C":
                result -= stack.pop()
            else:
                stack.append(int(operation))
                result += int(operation)
            print(stack)
            print(result)
        return result 