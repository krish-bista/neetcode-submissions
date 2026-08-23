class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)
        solution = []
        count = 0
        for str in strs:
            arr = [0] * 26
            for char in str:
                arr[ord(char) - ord('a')] += 1
            
            key = tuple(arr)
            hash[key].append(str)

        for key,value in hash.items():
            solution.append(value)
        
        return solution
        