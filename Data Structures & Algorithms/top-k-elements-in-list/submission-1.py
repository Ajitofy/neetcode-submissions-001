class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d1=dict()
        for i in nums:
            d1[i]=d1.get(i,0)+1
        return list(dict(sorted(d1.items(),key=lambda x:x[1],reverse=True)).keys())[:k]
