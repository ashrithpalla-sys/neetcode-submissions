class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        #buy = prices[0]
        #sell = prices[1]
        #profit = sell - buy

        #for i in range(2, len(prices)):
        #    p = prices[i]
        #    if p - buy > profit or p - sell > profit:
        #        if p - buy > p - sell:
        #            sell = p
        #            profit = sell - buy
        #        else:
        #            buy = sell
        #            sell = p
        #            profit = sell - buy
        
        b = prices[0]
        m = b
        s = prices[1]
        profit = s - b

        for i in range(1, len(prices)):
            p = prices[i]
            if p - m > profit:
                b = m
                s = p
                profit = s - b
            else:
                m = min(m, p)
            
        return max(profit, 0)
