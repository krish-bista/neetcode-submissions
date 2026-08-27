class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        i = 0
        j = 0
        mostFreq = 0
        longest = 0

        while j < len(s):
            seen[s[j]] = 1 + seen.get(s[j], 0) 
            mostFreq = max(mostFreq, seen[s[j]])

            while (j-i+1) - mostFreq > k:
                seen[s[i]] -= 1
                i += 1

            longest = max(longest, j - i + 1)
            j += 1           
        return longest
        