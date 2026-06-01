class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d1=dict()
        for i in nums:
            d1[i]=d1.get(i,0)+1
        l1=[[] for i in range(len(nums)+1)]

        for key,val in d1.items():
            l1[val].append(key)
        
        res=[]
        counter=k
        for j in range(len(l1)-1,-1,-1):
            if l1[j] and counter>0:
                for n in l1[j]:
                    res.append(n)
                    counter-=1
        return res