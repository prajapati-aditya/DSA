class Solution:
    def romanToInt(self, s: str) -> int:
        
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0   
        n = len(s)
        
        # Iterate
        for i in range(n):
            # Get value of current roman symbol
            value = roman_map[s[i]]
            
            
            if i + 1 < n and value < roman_map[s[i + 1]]:
                total -= value   # subtract if smaller before larger
            else:
                total += value   # otherwise, add normally
                
        return total

        