class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zp=-1   # zp = zero pointer pointing to first zero
        nzp=0   # non zero pointer
        for i in range(len(nums)):
            if nums[i] == 0:
                zp=i
                break
        if zp == -1:
            return nums
        
        for nzp in range(zp+1, len(nums)):
            if nums[nzp] != 0:
                nums[zp], nums[nzp] = nums[nzp], nums[zp]
                zp+=1
        return nums

        
