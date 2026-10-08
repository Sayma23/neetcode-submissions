class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        i = 0
        while i < len(s):
            if (s[i] == '(' or s[i] == '{' or s[i] == '['):
                stack.append(s[i])
            else:
                if(len(stack) == 0):
                    return False
                top = stack[-1] # check if length> 1
                if (s[i] == ')' and top == '('):
                    stack.pop()
                elif (s[i] == '}' and top == '{'):
                    stack.pop()
                elif (s[i] == ']' and top == '['):
                    stack.pop()
                else:
                    return False
            i += 1
        if(len(stack) == 0):
            return True
        else:
            return False   
