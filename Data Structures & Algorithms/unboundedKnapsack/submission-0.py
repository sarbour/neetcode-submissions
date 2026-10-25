class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        numRows, numCols = len(profit), capacity + 1
        dp = [[0] * numCols for _ in range(numRows)]

        for row in range(numRows):      # Item
            dp[row][0] = 0

        for col in range(numCols): # Capacity
            dp[0][col] = (col // weight[0]) * profit[0]

        for row in range(1, numRows):
            for col in range(numCols):
                skip = dp[row - 1][col]
                include = 0
                if col - weight[row] >= 0:
                    include = profit[row] + dp[row][col - weight[row]]
                dp[row][col] = max(include, skip)

        return dp[-1][-1]