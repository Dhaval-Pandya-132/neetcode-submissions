class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if len(stack) > 0 and ((c == "]" and stack[-1]== "[") or (c == ")" and stack[-1] == "(") or (c == "}" and stack[-1] == "{")):
                stack.pop()
            else :
                stack.append(c)
        return len(stack) == 0
