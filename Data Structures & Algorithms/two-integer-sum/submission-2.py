class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index = {}

        for i, num in enumerate(nums):
            compliment = target-num

            if compliment in num_index :
                return [num_index[compliment],i]

            else :
                num_index[num]= i

        return []
       


            

        