class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxi = prices[n-1]
        for i in range (n-1, -1, -1) :
            curr = prices [i]
            if curr <= maxi :
                prices[i] = maxi-curr
            else :
                prices[i] = 0
                maxi = curr
        return max(prices)
        