class Solution:
    def isValid(self, s : str) -> bool:
        stack = []
        parentheses = {')' : '(', '}' : '{', ']':'['}
        
        for char in s:
            if char in parentheses.values():
                stack.append(char)
            elif char in parentheses.keys():
                if len(stack) > 0 and stack[-1] == parentheses[char]:
                    stack.pop()
                else:
                    return False
        
        if not stack:
            return True
            
        return False
            


solution =  Solution()
s = "([})"
print(solution.isValid(s))