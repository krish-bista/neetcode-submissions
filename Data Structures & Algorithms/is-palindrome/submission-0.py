class Solution:
    def isPalindrome(self, s: str) -> bool:
        reversed = ""
        for i in range(len(s)-1, -1, -1):
            if not s[i].isalnum():
                continue
            reversed += s[i]
        
        s2 = ""
        for c in s:
            if not c.isalnum():
                continue
            s2 += c

        print(reversed)
        if s2.lower() == reversed.lower():
            return True
        return False