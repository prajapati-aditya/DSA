class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        buckets=[0,0,0]
        for num in nums :
            buckets[num]+=1
        
        i=0
        for num in range(3):
            for _ in range(buckets[num]):
                nums[i]=num
                i+=1
                
        return nums