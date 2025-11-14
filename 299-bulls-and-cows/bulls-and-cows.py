class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        bulls = 0
        cows = 0
        secret_freq = [0]*10
        guess_freq = [0]*10
        
        # getting no. of bulls 
        for s ,g in zip(secret,guess) :
            if g == s :
                bulls += 1
            else :
                secret_freq[int(s)] += 1
                guess_freq[int(g)] += 1 
        # counting cows :
        for i in range(10) :
            cows += min(secret_freq[i],guess_freq[i])
    
        return f"{bulls}A{cows}B"
            