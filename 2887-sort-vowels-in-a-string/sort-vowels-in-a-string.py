class Solution:
    def sortVowels(self, s: str) -> str:
        # extract all vowels present in s
        vowels=sorted([ch for ch in s if ch.lower() in "aeiouAEIOU"])
        vowel=set("aeiouAEIOU")
        # convert string into list for replacement
        chars=[]
        # now we 've a list so we will iterate and exchange the vowels in s
        index=0 # index for vowels list

        for ch in s :
            if ch in vowel :
                chars.append(vowels[index])
                index+=1
            else :
                chars.append(ch)
        return "".join(chars)
        
        