class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = {}
        for ch in s1:
            s1_map[ch] = s1_map.get(ch,0)+1

        l= 0 
        window ={}

        for right in range (len(s2)) :

            ch = s2[right]
            window[ch] = window.get(ch,0)+1
 
            if right - l +1 > len(s1):
                out = s2[l]
                window[out] -= 1
                if window[out] == 0 :
                    del window[out]

                l+=1

            if s1_map == window:
                return True 

        return False




        