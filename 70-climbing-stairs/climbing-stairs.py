class Solution:
    def climbStairs(self, n: int) -> int:
        def climb(n):
            if n==1:
                return 1
            if n==2:
                return 2
            step_1, step_2 = 1, 2

            for i in range(3,n+1):
                step_1, step_2 = step_2, step_1+step_2
            return step_2
        return climb(n)

        