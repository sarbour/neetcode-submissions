class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for word in strs:
            count = {}
            for c in word:
                count[c] = count.get(c, 0) + 1
            
            res[tuple(sorted(word))].append(word)

        return list(res.values())