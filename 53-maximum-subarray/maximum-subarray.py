class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        summ=nums[0]
        max_sum=nums[0]

        for i in range(1,len(nums)):
            summ=max (nums[i], summ+nums[i] )
            
            max_sum = max(summ, max_sum)

            
        return max_sum

        