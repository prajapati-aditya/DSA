class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
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

        