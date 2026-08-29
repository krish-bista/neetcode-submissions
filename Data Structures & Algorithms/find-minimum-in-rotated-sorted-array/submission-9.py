class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return min(nums[0], nums[1])
        l = 0
        r = len(nums)-1
        mid = (l + r) // 2
        while l < r:
            if nums[mid] < nums[mid-1] and nums[mid] < nums[mid+1]:
                return nums[mid]
            if nums[l] < nums[mid]:
                l = mid
            elif nums[mid] < nums[r]:
                r = mid
            elif r -l == 1:
                return min(nums[r], nums[l])
            mid = (l+r) // 2
        return nums[0]

           