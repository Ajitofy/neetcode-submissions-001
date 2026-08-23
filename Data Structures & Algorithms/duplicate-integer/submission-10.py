class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # brute force , for loop  , o(n2)
        # optimized
        d1 = dict()

        for i in nums:
            d1[i] = d1.get(i,0) + 1
        for k,v in d1.items():
            if v > 1:
                return True
        return False

