class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."]*n for _ in range (n)]
        sol = []
        # storing cols and diagonals
        col = set()
        diag1 = set()  # r-c
        diag2 = set() # r+c 

        def dfs(r) :
            # base case
            if r == n:
                temp = ["".join(row) for row in board]
                sol.append(temp)
                return

            for c in range(n) :
                if c in col or (r-c) in diag1 or (r+c) in diag2 :
                    continue
                board[r][c] = 'Q'
                col.add(c)
                diag1.add(r-c)
                diag2.add(r+c)
                # traverse for all
                dfs(r+1)
                # pop all
                board[r][c] ='.'
                col.remove(c)
                diag1.remove(r-c)
                diag2.remove(r+c)
        dfs(0)
        return sol
