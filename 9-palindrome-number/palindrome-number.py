class Solution:
    def isPalindrome(self, x: int) -> bool:
        a=x
        reverse=0
        while x>0:
            r=x%10
            reverse=reverse*10+r
            x=x//10
        print(reverse)
        if(reverse==a):
            return True
        else :
            return False   
        