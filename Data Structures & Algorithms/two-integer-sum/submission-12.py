class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d1=dict()

        for i in range(len(nums)):
            d1[nums[i]]=i
        
        for j in range(len(nums)):
            num = target-nums[j]
            if  (num  in d1) and (j!= d1[num]):
                return  [j,d1[num]]