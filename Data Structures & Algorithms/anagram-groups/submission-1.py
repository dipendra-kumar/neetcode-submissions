class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        strs_map = {}

        for i in range(len(strs)):
            sorted_word = "".join(sorted(strs[i])) 
            if sorted_word in strs_map:
                strs_map[sorted_word].append(strs[i])
            else:
                strs_map[sorted_word] = [strs[i]]

        return list(strs_map.values())