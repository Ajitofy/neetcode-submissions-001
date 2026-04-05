class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        1. run nested for loop,
        '''
        for i in range(len(nums)):
            for j in  range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    return True
        return False