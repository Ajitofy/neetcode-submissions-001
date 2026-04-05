class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l=0
        r=1
        res=[]
        while l<len(nums)-2:
            element=-(nums[l]+nums[r])
            if element in nums[r+1:]:
                res.append(sorted([nums[l],nums[r],element]))
            r+=1
            if r==len(nums):
                l+=1
                r=l+1
        l2=[]
        for i in (res):
            if i not in l2:
                l2.append(i)
            else:
                continue
        return l2
            
        