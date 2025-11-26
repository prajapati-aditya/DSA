class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        curr = []
        res = []
        n = len(candidates)
        seen= set()

        def solve(index,leftSum) :
            # base case
            if leftSum == 0 :
                res.append(curr.copy())
                return
            # termination
            if index >= n :
                return
            if candidates[index] > leftSum :
                return

            for i in range(index,n) :
                if i>index and candidates[i]==candidates[i-1]:
                    continue

                num = candidates[i]
                curr.append(num)
                seen.add(num)
                # recuse
                solve(i+1, leftSum-num)
                # backtrack
                curr.pop()
                
        solve(0,target)
        return res