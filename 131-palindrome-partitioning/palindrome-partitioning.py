class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr = []

        def backtrack (index):
            if index == len(s) :
                res.append(curr.copy())
            
            for j in range(index, len(s)) :
                if self.IsPalindrome(s, index, j) :
                    curr.append (s[index:j+1])
                    backtrack(j+1)
                    curr.pop()
        
        backtrack(0)
        return res
    # helper function
    def IsPalindrome(self, s, l, r) :
        
        while l<r :
            if s[l] != s[r] :
                return False
            l+=1
            r-=1
        return True