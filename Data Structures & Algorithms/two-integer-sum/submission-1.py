class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup ={}
        n = len(nums)
        result =[]
        for i in range(n):
            compliment  = target - nums[i]
            if compliment in lookup:
                result = [lookup[compliment], i]
            
            lookup[nums[i]] = i
        return result