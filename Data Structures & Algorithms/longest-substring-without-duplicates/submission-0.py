class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        seen = set()
        l = 0

        for i, c in enumerate(s):
            while c in seen and l <= i:
                seen.remove(s[l])
                l += 1
            
            seen.add(c)
            res = max(res, len(seen))

        return res