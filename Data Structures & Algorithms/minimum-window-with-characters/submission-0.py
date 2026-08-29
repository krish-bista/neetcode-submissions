class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        freqt = {}
        for i in range(len(t)):
            freqt[t[i]] = 1 + freqt.get(t[i], 0)
        

        need = len(freqt)
        have = 0
        window = {key:0 for key in freqt.keys()}
        i = 0
        res, resLen = [-1, -1], float("infinity")
    
        for j in range(len(s)):
            window[s[j]] = 1 + window.get(s[j], 0)
            
            if s[j] in freqt and window[s[j]] == freqt[s[j]]:
                have += 1
            
            while have == need:
                if (j - i + 1) < resLen:
                    res = [i, j]
                    resLen = (j - i + 1)
                
                window[s[i]] -= 1
                if s[i] in freqt and window[s[i]] < freqt[s[i]]:
                    have -= 1
                i += 1
            
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""
