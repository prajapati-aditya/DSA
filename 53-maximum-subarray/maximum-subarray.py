class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=float('-inf')
        curr=0
        for i in nums:
            curr=curr+i
            max_sum=max(max_sum,curr)
            if curr<0:
                curr=0
        return max_sum
        ''' summ=nums[0]
        max_sum=nums[0]

        for i in range(1,len(nums)):
            summ=max (nums[i], summ+nums[i] )
            
            max_sum = max(summ, max_sum)

            
        return max_sum '''


        