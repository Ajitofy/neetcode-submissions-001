class Solution:
    def maxProfit(self, arr: List[int]) -> int:
        l=0
        r=1
        n=len(arr)
        max_profit=0
        while r<n:
            if arr[r]<arr[l]:
                l=r
                r+=1
            else:
                profit=arr[r]-arr[l]
                max_profit=max(profit,max_profit)
                r+=1
        return max_profit
                

        return max_profit