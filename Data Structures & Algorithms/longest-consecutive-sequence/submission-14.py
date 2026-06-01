class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s1=set()
        count=0
        maxCount=0
        for i in nums:
            s1.add(i)
        
        for i in nums:
            temp=i
            if temp-1 not in s1:
                count=1
                if temp in s1:
                    s1.remove(temp)
                while temp+1 in s1:
                    count+=1
                    s1.remove(temp+1)
                    temp+=1
            maxCount=max(maxCount,count)
        return maxCount
