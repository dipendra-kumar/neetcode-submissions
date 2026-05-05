class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
        
        for char in s: 
            counter[char] += 1

        for char in t: 
            counter[char] -= 1

        for count in counter.values():
            if count != 0: 
                return False
        return True


