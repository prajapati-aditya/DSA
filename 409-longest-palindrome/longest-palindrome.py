from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)
        odd = False
        res = 0
        for count in freq.values() :
            if count % 2 == 0:
                res += count
            else :
                res += count-1
                odd = True
        if odd :
            res += 1
        return res
        