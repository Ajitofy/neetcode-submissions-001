class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
            
            d1=defaultdict(list)
            s1=set(nums)
            longest=0
            for i in nums:
                length=0
                if i-1 not in s1:
                    while i+length in s1:
                        length+=1
                    longest=max(longest,length)
            return longest    

