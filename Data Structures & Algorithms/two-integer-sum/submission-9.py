class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d1=dict()
        for i, n in enumerate(nums):
            d1[n]=i
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in d1 and i!=d1[diff]:
                return [i,d1[diff]]
        return[]