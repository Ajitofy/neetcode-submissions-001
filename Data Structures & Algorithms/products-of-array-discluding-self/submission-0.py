class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res=[]
        for i in range(len(nums)):
            l1=nums.copy()
            l1.remove(nums[i])
            mul=1
            for j in l1:
                mul*=j
            res.append(mul)
        return res