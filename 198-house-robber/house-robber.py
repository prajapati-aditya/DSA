class Solution:
    def rob(self, nums: List[int]) -> int:
        # dict to store value calculated to be used later
        memo={}
        def robber(nums,index):
            # we will use dp concept top down memoization
            if index >= len(nums):
                return 0
            
            # check if value already exist in dictionary
            if index in memo :
                return memo[index]
            
            rob_it = nums[index] + robber(nums, index+2)
            skip_it = 0+ robber(nums, index+1)

            memo[index]= max(rob_it, skip_it)
            return memo[index]
        return robber(nums, 0)
            

            
'''
            time limit exceeded
             # base case
            if index >= len(nums):
                return 0
            
            opt_1 = nums[index] + robber(nums, index+2)

            opt_2 = 0 + robber(nums, index+1)

            return max(opt_1, opt_2)
        return robber(nums,0) 
        '''
