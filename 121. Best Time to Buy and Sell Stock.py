class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #Initution: This is a sliding window question w/ variable window length
        # You are trying to get lowest value for buy
        # Get highest value for sell
        # 1) Find when prices[buy] < prices[sell]
        # 2) If prices[sell] > prices[buy], check if its profit is better than max_profit
        # 3) Else: go to next smaller buy value to potentionally get better profit
        buy = 0
        sell = 1
        n = len(prices)
        max_profit = 0
        while(sell < n): 
            if prices[buy] < prices[sell]:
                max_profit = max(prices[sell] - prices[buy], max_profit)
            else:
                # There exist smaller buy value than curr
                buy = sell
            
            sell += 1
        return max_profit