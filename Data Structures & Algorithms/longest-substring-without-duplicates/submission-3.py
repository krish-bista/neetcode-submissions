class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        longest = 0
        
        i = 0
        j = 0
        while j < len(s):
            if s[j] not in seen:
                seen[s[j]] = True
                j += 1

            else:
                del seen[s[i]]
                i += 1

            length = j - i
            longest = max(length, longest)            
        
        return longest