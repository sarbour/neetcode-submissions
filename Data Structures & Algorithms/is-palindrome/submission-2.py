class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "":
            return True
        
        sAlphaNum = []

        for c in s:
            if c.isalnum():
                sAlphaNum.append(c.lower())

        temp = "".join(sAlphaNum)

        l, r = 0, len(temp) - 1

        while (l < r and temp[l] == temp[r]):
            l += 1
            r -= 1

        return r <= l