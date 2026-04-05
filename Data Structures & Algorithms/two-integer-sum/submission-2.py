class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d1=dict()
        for i in range(len(nums)):
            first_no=target-nums[i]
            if first_no in d1:
                return [d1[first_no],i]
            if nums[i] not in d1:
                d1[nums[i]]=i
            
            


        
        