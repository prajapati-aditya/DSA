class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        curr=[]
        total=0

        def backtrack(index,curr,total):
            # base cases:
            if total==target:
                res.append(curr.copy())
                return
            if index>= len(candidates) or total>target :
                return
            # pick 
            curr.append(candidates[index])
            backtrack(index,curr,total+candidates[index])

            # before not pick remove the top element
            curr.pop()
            # not pick
            backtrack(index+1,curr,total)

        backtrack(0,[],0)
        return res