class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict1 = { ")" : "(",
                "]" : "[",
                "}" : "{"
        }
        for char in s :
            if char in dict1 :
                if stack and stack[-1] == dict1[char] :
                    stack.pop()
                else :
                    return False
            
            else :
                stack.append(char)
        if len(stack) == 0 :
            return True
        else :
            return False
        