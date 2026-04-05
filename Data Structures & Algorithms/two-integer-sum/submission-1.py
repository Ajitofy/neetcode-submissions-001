class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=0
        r=1
        n=len(nums)
        prevMap={}
        
        for i,e in enumerate(nums):
            diff=target-nums[i]
            if diff in prevMap:
                return [prevMap[diff],i]
            
            prevMap[e]=i
        