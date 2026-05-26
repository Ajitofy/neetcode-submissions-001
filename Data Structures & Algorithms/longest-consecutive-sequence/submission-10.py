class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums.sort()
        max_seq = 0
        curr_seq=1
        curr=0
        next=1

        while curr <( len(nums)-1):
            if (nums[curr] + 1) == nums[next]:
                curr_seq+=1

            max_seq=max(curr_seq,max_seq)

            if nums[curr]==nums[next]:
                curr+=1
                next+=1
                continue
            if (nums[curr] + 1) != nums[next]:
                curr_seq=1
                
            curr+=1
            next+=1
        max_seq=max(curr_seq,max_seq)      
        return max_seq