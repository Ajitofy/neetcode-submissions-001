class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d1={}
        if nums:
            for i in nums:
                d1[i]=d1.get(i,0)+1
            if max(d1.values())>1:
                return True
            else:
                return False
        else:
            return False 