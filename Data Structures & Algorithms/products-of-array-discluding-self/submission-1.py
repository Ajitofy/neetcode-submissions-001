class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        # res=[0]*n
        prefix=[0]*n
        suffix=[0]*n

        prefix[0]=suffix[n-1]=1
        result=1
        for i in range(n):
            prefix[i]=result*nums[i]
            result=prefix[i]
            if i==n-1:
                result=1

        for j in range(n-1,-1,-1):
            suffix[j]=result*nums[j]
            result=suffix[j]
        
        for i in range(n):
            if i==0:
                nums[i]=1*suffix[i+1]
            elif i==n-1:
                nums[i]=prefix[i-1]*1
            else:
                nums[i]=prefix[i-1]*suffix[i+1]
        return nums
        

















