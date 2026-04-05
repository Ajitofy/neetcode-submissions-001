class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=0
        r=1
        n=len(nums)
        while r<n:
            if nums[l]+nums[r]==target:
                return [l,r]
            else:
                if r==n-1:
                    l+=1
                    r=l+1
                else:
                    r+=1