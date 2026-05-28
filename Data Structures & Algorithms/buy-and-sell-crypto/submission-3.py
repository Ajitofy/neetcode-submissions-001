class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l=0
        if len(prices)>1:
            r=1
        else:
            r=0

        while l<r:
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit,profit)
                if r==len(prices)-1:
                    l+=1
                else:
                    r+=1
            else:
                if r==len(prices)-1:
                    l=l+1
                else:
                    l=r
                    r+=1
                
        return max_profit