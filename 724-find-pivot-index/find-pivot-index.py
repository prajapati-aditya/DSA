class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0 
        total = sum(nums)
        for ind, num in enumerate(nums) :
            if left_sum == total - ( left_sum + num ) :
                return ind
            left_sum += num
        return -1
        