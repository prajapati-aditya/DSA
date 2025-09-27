class Solution:
    def reverseWords(self, s: str) -> str:
        words= s.split()        #split and make array of words
        stack =[]
        for string in words :       # push into stack
            stack.append(string)
        
        reversed=[]
        while stack :
            reversed.append(stack.pop())        # popo and join to reverse the string

        return " ".join(reversed)