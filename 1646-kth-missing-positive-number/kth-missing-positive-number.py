class Solution:
    def findKthPositive(self, arr, k):
        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid = (left + right) // 2
            missing = arr[mid] - (mid + 1)

            if missing < k:
                left = mid + 1
            else:
                right = mid - 1
        
        # After loop, 'right' is last index where missing < k
        # kth missing = k + right + 1
        return k + right + 1

        