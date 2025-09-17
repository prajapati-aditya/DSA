class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # optimal solution
        n=len(nums)
        ans=[0]*n # == [0,0,0,0,0,0]
        pos = 0
        neg = 1
        for i in range(n):
            if nums[i] > 0:
                ans[pos] = nums[i]
                pos+=2
            else :
                ans[neg] = nums[i]
                neg+=2
        return ans


        # brute force approach
'''                
        n = len(nums)//2
        pos= []
        neg = []

        l=0
        r=0
        for i in range(len(nums)):
            if nums[i] > 0:
                pos.append(nums[i])
                
            else :
                neg.append(nums[i])
                

        l,r=0,0
        i=0
        while i < len(nums):
            nums[i] = pos[l]
            i+=1
            l+=1
            nums[i] = neg[r] 
            i+=1
            r+=1
        return nums
'''

        