class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        completes = {"()":True, "{}":True, "[]":True}
        for i in range(len(s)):
            stack.append(s[i])
            if stack[len(stack)-2] + s[i] in completes:
                stack.pop(len(stack)-1)
                stack.pop(len(stack)-1)
        
        if len(stack) == 0:
            return True
        return False