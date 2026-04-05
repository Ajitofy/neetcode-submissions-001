class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        1. Initiate variable i = 0
        2. if condition where no = val, decremetn n by 1, 
        replace ith element with nth
        3. if  no != val , incremet i by 1
        """
        i=0
        n=len(nums)
        while i<n:
            if nums[i]==val:
                n-=1
                nums[i]=nums[n]
                continue
            i+=1
        return n