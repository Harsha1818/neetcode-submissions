class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0 or s == " ":
            return True
        lo = 0 
        hi = len(s) - 1

        while hi>lo :

            while lo<hi and not s[lo].isalnum():
                lo +=1

            while lo<hi and not s[hi].isalnum():
                hi -= 1

            if s[hi].lower() != s[lo].lower():
                return False 

            hi -= 1
            lo += 1
            
        return True 



        