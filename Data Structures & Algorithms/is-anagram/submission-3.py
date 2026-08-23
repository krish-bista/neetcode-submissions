class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash = {}

        for char in s:
            if char in hash:
                hash[char] += 1
            else:
                hash[char] = 1

        for char in t:
            if char not in hash:
                return False
            else:
                hash[char] -= 1

        for item in hash:
            if hash[item] != 0:
                return False
        return True