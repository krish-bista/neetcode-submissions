class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        hash = {}
        for i in range(len(nums)):
            hash[nums[i]] = i
        
        for i in range(len(nums)):
            if( target - nums[i] in hash) and (i != hash[target-nums[i]]):
                return [min(i, hash[target-nums[i]]), max(i, hash[target-nums[i]])]