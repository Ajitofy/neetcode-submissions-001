class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        forward =[1]
        mul = 1
        for i in range(len(nums)-1):
            mul*=nums[i]
            forward.append(mul)

        backward = [1]
        mul = 1
        for i in range(len(nums)-1,0,-1):
            mul*=nums[i]
            backward.insert(0,mul)
        res=[]
        for j in range(len(forward)):
            res.append(forward[j]*backward[j])
        return res