class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1. Brute Force: Time Complexity- O(n2), Space Complexity- O(1) 
        # for i in range(len(nums)):
        #     diff=target-nums[i]
        #     for j in range(i+1,len(nums)):
        #         if diff == nums[j]:
        #             return [i,j]
        
        # 2. Optimized with TC- O(n) SC-O(n)
        d1=dict()
        for i,num in enumerate(nums):
            d1[num]=i
        for j,num in enumerate(nums):
            diff=target-num
            if diff in d1 and d1[diff] !=j:
                return  [j,d1[diff]]

        