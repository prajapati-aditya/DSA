class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        check = set ()

        def backtrack (nums,curr):
            if len(curr) == len(nums) :
                res.append(curr.copy())
                return
            
            for i in range(len(nums)) :
                if nums[i] not in check :
                    curr.append(nums[i])
                    check.add(nums[i])

                    backtrack(nums, curr)
                    curr.pop()
                    check.discard(nums[i])
            
        backtrack(nums,curr)
        return res