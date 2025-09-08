class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def checkZero(num):
            while num>0:
                if (num%10)==0:
                    return False
                num=num//10
            return True
        i=1
        while i<=n :
            if checkZero(i) and checkZero(n-i):
                return[i,n-i]
            i+=1
            
            
                  