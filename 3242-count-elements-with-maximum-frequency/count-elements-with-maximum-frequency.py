from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dict = Counter(nums)
        res = 0
        max_freq = 1
        for num in dict.values() :
            if num > max_freq :
                max_freq = num
        for key, value in dict.items() :
            if value == max_freq :
                res += value
        return res
        