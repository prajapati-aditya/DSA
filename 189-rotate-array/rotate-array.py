class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        # first reverse whole array
        l=0
        r=len(nums)-1
        while l<r :
            nums[l], nums[r] = nums[r], nums[l]
            l,r= l+1, r-1

        # second reversal from 0 to k'th element
        l, r = 0, k-1
        while l< r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l+1, r-1
        
        #third reversal k'th element to the last element
        l,r=  k,len(nums)-1
        while l< r:
            nums[l], nums[r] = nums[r], nums[l]
            l,r = l+1,r-1
        
        return nums
        