class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = float('-inf')
        l , r = 0, len(height)-1
        while l <= r :
            # mini = min(height[l] , height[r])
            # area = max(area , mini*(r-l))
            if height[l] <= height[r] :
                area = max( area, height[l] * (r-l) )
                l+=1
            else :
                area = max( area, height[r] * (r-l) )
                r -= 1
        return area
        