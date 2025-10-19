import math

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)
        ans = right

        while left <= right:
            mid = (left + right) // 2
            total = sum(math.ceil(num / mid) for num in nums)

            if total <= threshold:
                ans = mid
                right = mid - 1   # try smaller divisor
            else:
                left = mid + 1    # need larger divisor
        
        return ans
