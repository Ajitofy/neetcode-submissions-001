class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d1=dict()
        for i in range(len(nums)):
            d1[nums[i]] = i
        
        for j in range(len(nums)):
            second = target - nums[j]

            if (second in d1) and (d1[second] != j):
                return [j,d1[second]]
