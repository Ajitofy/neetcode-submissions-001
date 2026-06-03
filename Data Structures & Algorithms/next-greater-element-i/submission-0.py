class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[-1]*len(nums1)
        stack=[]
        d1= dict()
        for i,n in enumerate(nums1):
            d1[n]=i
        for i in range(len(nums2)):
            while stack and nums2[i]>stack[-1]:
                val=stack.pop()
                idx=d1[val]
                res[idx]=nums2[i]
            if nums2[i] in d1:
                stack.append(nums2[i])
        return res

        
