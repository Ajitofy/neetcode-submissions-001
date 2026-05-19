class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d1=dict()

        for i, num in enumerate(nums):
            two = target-num
            if two in d1:
                return [d1[two],i]
            d1[num]=i