class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        # edge cases :
        if len(nums) <= 2:
            return len(nums)
        n=len(nums)
        maxi = nums.index(max(nums))
        mini = nums.index(min(nums))
        if maxi < mini :
            mini ,  maxi = maxi , mini 
        
        # remove from front 
        front = max(maxi ,  mini ) +1
        back = max(n-maxi ,  n-mini)
         # removing from both sides
        both = (mini+1) + (n-maxi)
        return min(front, back, both)
