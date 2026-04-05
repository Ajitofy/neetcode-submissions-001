class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s1=set(nums)
        res=0

        for num in nums:
            streak,curr=0,num
            while curr in s1:
                curr+=1
                streak+=1
            res=max(streak,res)
        return res