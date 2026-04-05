class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d1={}
        for i in nums:
            d1[i]=d1.get(i,0)+1
        final_list=sorted(d1.keys(),key=lambda x:d1[x],reverse=True)
        return final_list[:k]