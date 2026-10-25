class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {} # number –> frequency

        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        freqSort = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        res = []

        for i in range(k):
            res.append(freqSort[i][0])

        return res
