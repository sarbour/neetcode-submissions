class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos = {}
        
        for i, n in enumerate(nums):
            pos[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if (diff) in pos and pos[diff] != i:
                return [i, pos[diff]]

        return []