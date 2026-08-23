class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d1 = dict()

        for i in range(len(nums)):
            d1[nums[i]] = i
        
        for j in range(len(nums)):
            num2 = target - nums[j]

            if num2 in d1 and d1[num2] != j:
                return [j, d1[num2]]