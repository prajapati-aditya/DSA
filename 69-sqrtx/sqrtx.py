class Solution:
    def mySqrt(self, x: int) -> int:
        # edge case if 
        if x < 2:
            return x
        l = 0
        r = x//2
        while l <= r :
            mid = (l+r) //2
            num = mid * mid

            if num == x :
                return mid
            elif num < x :
                l = mid+1
            else :
                r = mid-1
        return r