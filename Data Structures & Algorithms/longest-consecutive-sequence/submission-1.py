class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        hash = {}
        for num in nums:
            hash[num] = True
        
        longest = 1
        curr = 1

        for num in nums:
            if num -1 not in hash:
                curr = 1
                while (num + 1) in hash:
                    curr += 1
                    num += 1
                if curr > longest:
                    longest = curr

        return longest