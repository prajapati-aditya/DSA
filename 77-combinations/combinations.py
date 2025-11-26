class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        temp = []
        sol = []

        def backtrack(index) :
            # base condn
            if len(temp) == k :
                sol.append(temp.copy())
                return
            if index > n :
                return

            for i in range(index,n+1) :
                temp.append(i)

                backtrack(i+1)
                
                temp.pop()

        backtrack(1)
        return sol