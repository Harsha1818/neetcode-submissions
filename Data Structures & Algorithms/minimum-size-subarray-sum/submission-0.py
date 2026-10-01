class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # visited = {5:2, 1:3,5:4}  cs m= 11 if cs >= target length= 3
        
        #   left =3 right = 4
        

        ## 2+1 +5+1+5.  c= 14 -nums[left] = 10

        left = 0
        best = float('inf')
        s= 0 

        for right in range(len(nums)):
            s += nums[right]

            while s >= target :
                best = min (best, right-left+1)
                s-= nums[left]
                left+=1 

        return best if best != float('inf') else 0 

