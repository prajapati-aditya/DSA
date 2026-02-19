class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # counting subgroups
        # s = 00 11 00 11 => 2 2 2 2
        # o/p = min(2,2) + min(2,2) + min (2,2) 
        prev = 0    # prev grp
        curr = 1    # curr grp
        ans = 0
        for i in range(1,len(s)) :
            if s[i] == s[i-1] :
                curr += 1
            else :
                ans += min(prev,curr)
                prev = curr
                curr = 1
        ans += min(curr,prev)
        return ans