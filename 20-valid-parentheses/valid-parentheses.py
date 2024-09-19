class Solution:
    def isValid(self, s: str) -> bool:
        stack = list(range(len(s)))
        top = -1
        for i in s:
            if (i == '(') or (i=='{') or (i=='['):
                top = top +1
                stack[top]=i
            elif (i == ')' and stack[top]=='(') or (i == ']' and stack[top]=='[') or(i == '}' and stack[top]=='{'):
                top= top-1
            else:
                return False
        if (top == -1):
            return True
        else:
            return False
                
                
