class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_res=0
        i=0
        n=len(nums)
        d1=dict()
        d2=dict()
        for num in nums:
            d1[num]=d1.get(num,0)+1
        for k,v in d1.items():
            d2[v]=k
        return d2[max(d2.keys())]
                
