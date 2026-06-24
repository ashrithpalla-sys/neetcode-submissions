class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        
        stack = []
        start = {'(', '{', '['}
        end = {')', '}', ']'}
        
        for c in s:
            if c in start:
                stack.append(c)
            if c in end:
                if not stack:
                    return False
                elif c == ')' and stack[-1] == '(':
                    stack.pop()
                elif c == '}' and stack[-1] == '{':
                    stack.pop()
                elif c == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
        
        if not stack:
            return True
        return False