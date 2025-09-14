class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        min_time=float('inf')
        for ch in tasks :
            summ= sum(ch)
            min_time = min(min_time,summ)
        return min_time
        