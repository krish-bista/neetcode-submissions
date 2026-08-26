class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        i = 0
        j = len(nums) - 1
        output = []

        for i in range(len(nums)):
            j = i+1
            k = len(nums) - 1
            target = -nums[i]
            while j < k:
                twosum = nums[j] + nums[k]
                if twosum == target:
                    output.append(tuple([nums[i], nums[j], nums[k]]))
                    j += 1
                elif twosum < target:
                    j += 1
                else:
                    k -= 1
            
        return list(set(output))
        