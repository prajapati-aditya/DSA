class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        curr=[]
        candidates.sort()
        def back(index,target):
            if target==0 :
                res.append(curr[:])
                return
            
            for i in range(index,len(candidates)):
                if i>index and candidates[i]==candidates[i-1]:
                    continue
                elif candidates[i]>target:
                    break
                curr.append(candidates[i])
                back(i+1,target-candidates[i])
                curr.pop()
            
            
        back(0,target)
        return res