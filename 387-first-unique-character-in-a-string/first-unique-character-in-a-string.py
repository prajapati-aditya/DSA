from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = Counter(s)
        arr = list(s)
        for ind, string in enumerate (arr) :
            if freq[string] == 1:
                return ind
        return -1