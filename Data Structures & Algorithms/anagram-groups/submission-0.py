class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result  = []

        strs_copy = []
        for i in range(len(strs)):
            sorted_word = sorted(strs[i])
            strs_copy.append(sorted_word)
        
        for i in range(len(strs_copy)):
            if strs[i] == '#': continue
            current = [strs[i]]
            for j in range(i, len(strs_copy)):
                if i == j: continue
                if strs_copy[i] == strs_copy[j]:
                    current.append(strs[j])
                    strs[j] = "#"

            result.append(current)
        return result