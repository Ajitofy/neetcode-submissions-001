class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            temp=nums.copy()
            temp.pop(i)
            mul = 1
            # nums2 = nums.pop(i)
            for j in temp:
                mul *= j
            res.append(mul)
        return res