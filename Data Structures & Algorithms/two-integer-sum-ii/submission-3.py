class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        curr = 0
        next = 1

        while curr < len(numbers):
            for i in range(curr+1,len(numbers)):
                if numbers[curr]+numbers[i]==target:
                    return [curr+1,i+1]
            curr+=1
        
