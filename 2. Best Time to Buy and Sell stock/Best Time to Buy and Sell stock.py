class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left = 0
        right = 1
        max_profit = 0
        while left < right and right < len(prices):
            current_profit = prices[right] - prices[left]
            if current_profit > max_profit:
                max_profit = current_profit
                print(max_profit)
            elif prices[right] < prices[left]:
                left = right
            right+=1

        return max_profit