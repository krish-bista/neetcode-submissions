class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        bucket = [[] for i in range(len(nums) + 1)]
        solution = []

        for num in nums:
            if num in hash:
                hash[num] += 1
            else:
                hash[num] = 1

        for n, c in hash.items():
            bucket[c].append(n)
        
        for i in range(len(bucket)-1, 0, -1):
            for n in bucket[i]:
                solution.append(n)
                if len(solution) == k:
                    return solution
        
    


