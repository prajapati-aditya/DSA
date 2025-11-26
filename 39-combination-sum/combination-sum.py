class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        curr = []
        res = []
        n = len(candidates)
        candidates.sort()
        
        def solve(index, leftSum) :
            # base case
            if leftSum == 0 :
                res.append(curr.copy())
                return
            # termination
            if candidates[index] > leftSum :
                return
            

            for i in range(index,n) :
                num = candidates[i]
                curr.append(num)
                # recurse
                solve(i,leftSum-num)
                # backtrack
                curr.pop()
        
        solve(0,target)
        return res