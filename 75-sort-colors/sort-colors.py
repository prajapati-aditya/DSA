class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        yes I'll do, don't you worry
        """
        # DNF
        low = 0
        mid = 0
        high = len(nums) - 1
        while mid <= high :
            if nums[mid] == 0 :
                nums[low] , nums[mid] = nums[mid] , nums[low]
                low += 1
                mid += 1
            
            elif nums[mid] == 1 :
                mid += 1 
            
            else :    # means other than 0 and 1 is 2
                nums[mid] , nums[high] = nums[high] , nums[mid]
                high -= 1
        return nums


        