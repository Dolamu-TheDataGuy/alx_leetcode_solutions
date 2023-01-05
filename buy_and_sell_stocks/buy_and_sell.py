from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit_list = [0]

        if len(prices) < 2:
            return 0
        
        
        for i in range(0, len(prices)-1):
            if prices[i] >= prices[i+1]:
                continue
            elif prices[i] < prices[i+1]:
                for x in range(i + 1, len(prices)):
                    profit  = prices[x] - prices[i]

                    if profit > profit_list[0]:
                        profit_list[0] = profit
            else:
                return 0
        return profit_list[0]


price = [7,1,5,3,6,4]

if __name__ == "__main__":
    clod = Solution()
    print(clod.maxProfit(price))
