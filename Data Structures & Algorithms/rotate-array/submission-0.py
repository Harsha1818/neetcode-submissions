class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n= len(nums)
        k = k%n

        if k == 0 :
            return 

        def reverse (lo,hi):
            while lo<hi:
                nums[lo], nums[hi] = nums[hi],nums[lo]
                hi -= 1
                lo += 1

            
        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)


        