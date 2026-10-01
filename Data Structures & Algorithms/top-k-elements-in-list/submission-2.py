class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = {}
        res = []

        for num in nums:
            if num in frequency_map :
                frequency_map[num]+=1

            else :
                frequency_map[num] = frequency_map.get(num,0)+1

        ordered = sorted(
            frequency_map,
            key =frequency_map.get,
            reverse = True
        )

        return ordered[:k]
