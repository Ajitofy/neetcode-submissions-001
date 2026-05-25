class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d1 = dict()

        for i in nums:
            d1[i]=d1.get(i,0)+1
        

        l1 = []
        for _ in range(k):
            max_freq = float('-inf') 
            most_freq = float('-inf') 
            for k,v in d1.items():
                if max_freq < v:
                    max_freq = v
                    most_freq = k

            l1.append(most_freq)

            del d1[most_freq] 

        return l1      