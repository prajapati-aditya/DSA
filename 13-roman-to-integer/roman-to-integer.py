class Solution:
    def romanToInt(self, s: str) -> int:
        # Step 1: Mapping of roman numerals to integers
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0   # final result
        n = len(s)
        
        # Step 2: Iterate through string
        for i in range(n):
            # Get value of current roman symbol
            value = roman_map[s[i]]
            
            # Step 3: Check lookahead (is next value bigger?)
            if i + 1 < n and value < roman_map[s[i + 1]]:
                total -= value   # subtract if smaller before larger
            else:
                total += value   # otherwise, add normally
                
        return total

        