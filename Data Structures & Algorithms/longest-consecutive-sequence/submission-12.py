class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s1=set(nums)
        curr_seq = 0
        max_seq=0
        i=0
        while i < len(nums):
            if nums[i]-1  not in s1:
                curr_seq=1
                j=nums[i]
                while (j+1 in s1) :
                    curr_seq+=1
                    j+=1
                    
                max_seq=max(curr_seq,max_seq)
            i+=1
        # max_seq=max(curr_seq,max_seq)
        return max_seq

