class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        best = 0 
        max_frequency = 0 
        left = 0 

        for right in range (len(s)):

            count[s[right]] = count.get(s[right],0) +1 
            max_frequency = max(count[s[right]], max_frequency)
            win = right - left +1 

            if win- max_frequency > k :
                count[s[left]] -= 1
                left += 1

            best = max(best, (right - left +1))

        return best  

        

        