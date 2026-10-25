class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        memo = {}
        
        def dfs(i, curCap):
            if i == len(profit):
                return 0

            maxProfit = dfs(i + 1, curCap)

            newCap = curCap - weight[i]

            if newCap >= 0:
                p = profit[i] + dfs(i + 1, newCap)
                maxProfit = max(maxProfit, p)

            return maxProfit

        return dfs(0, capacity)