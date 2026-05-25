class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        res = []

        l1 = [[] for i in range(len(nums)+1)]

        d1 = dict()

        for i in nums:
            d1[i] = d1.get(i,0) + 1
        
        for item, freq in d1.items():
            l1[freq].append(item)
        
        for i in range(len(l1)-1,-1,-1):
            
            for j in l1[i]:
                res.append(j)
                k-=1
                if k==0:
                    return res