from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        for i in range (len(nums)) :
            # if not in window :
            if q and q[0] == i-k :
                q.popleft()
            # if found greater element, then empty queue
            while q and nums[q[-1]] <= nums[i] :
                q.pop()
            q.append(i)
            if i >= k-1 :
                res.append(nums[q[0]])
        return res
        
        ''' T.L.E
        l=0
        r=k-1
        res=[]
        while r <len(nums) :
            maxi = max(nums[l:r+1])
            res.append(maxi)
            l+=1
            r+=1
        return res
        '''

        