class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sol=[]
        result=[]

        def backtrack(index):
            if index==len(nums):
                result.append(sol[:])
                return
            # don't pick
            sol.append(nums[index])
            backtrack(index+1)

            #don't pick
            sol.pop()
            backtrack(index+1)
            
        # call the function 
        backtrack(0)
        return result