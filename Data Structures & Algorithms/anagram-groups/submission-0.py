class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}

        for s in strs:
            key = "".join(sorted(s))

            if key in anagram:
                anagram[key].append(s)
            else:
                anagram[key] = [s]

        return list(anagram.values())