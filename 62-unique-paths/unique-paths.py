class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # memoization 
        cache = [[-1 for _ in range (n)] for _ in range (m) ]

        def path(i , j ) :
            if i == m-1 and j == n-1 :
                return 1
            if i < 0 or i >= m or j < 0 or j >= n :
                return 0
            if cache[i][j] != -1 :
                return cache[i][j]
            else :
                right = path(i , j+1)
                down = path(i+1 , j)
                cache[i][j] = right+down
                return cache[i][j]
        # call the function
        return path(0,0)        
        
        '''     # recursive solution time limit exceeded

        def path(i,j):
            if i==m-1 and j== n-1 :
                return 1
            if i<0 or i>= m or j< 0 or j>= n :
                return 0
            right = path(i, j+1)
            left = path(i+1, j)
            return right+left
        return path(0,0)
        '''      
                  
        