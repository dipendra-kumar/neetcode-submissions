class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = set(nums)
        return len(list(unique)) != len(nums)