class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        curr= []
        res=[]
        def back(index,k,n):
            if k==0 and n==0:
                res.append(curr[:])
                return 
            
            if k==0 or n<=0 :
                return
            for i in range(index,10):
                curr.append(i)
                back(i+1,k-1,n-i)
                curr.pop()
        back(1,k,n)
        return res