class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # tuple(sorted(freq.items())) -> List

        for word in strs:
            freq = {}
            for c in word:
                freq[c] = 1 + freq.get(c, 0)

            res[tuple(sorted(freq.items()))].append(word)

        return list(res.values())