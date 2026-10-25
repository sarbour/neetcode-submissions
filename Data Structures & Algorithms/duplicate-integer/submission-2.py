class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = set(nums)

        return len(freq) != len(nums)