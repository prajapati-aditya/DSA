class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums :
            if num in freq :
                freq[num] += 1
            else :
                freq[num] = 1
        bucket = [[] for _ in range(len(nums) + 1)]
                
        for num, count in freq.items():
            bucket[count].append(num)
            


        # traverse from back 
        res = []
        count = 0
        for i in range(len(bucket)-1 , -1 ,-1) :
            for num in bucket[i] :
                res.append(num)
                count += 1
            if count == k :
                return res