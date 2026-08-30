class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        mid = (l+r) // 2

      

        while True:
            if nums[mid] == target:
                return mid
            if nums[l] < nums[mid]:
                if target >= nums[l] and target <= nums[mid]:
                    r = mid
                else:
                    l = mid
            
            elif nums[mid] < nums[r]:
                if target >= nums[mid] and target <= nums[r]:
                    l = mid
                else:
                    r = mid

            if (r-l) <= 1:
                if nums[r] == target:
                    return r
                elif nums[l] == target:
                    return l
                else:
                    return -1
            mid = (l+r) //2
        
