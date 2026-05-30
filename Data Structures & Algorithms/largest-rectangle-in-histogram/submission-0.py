class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea=0
        n=len(heights)
        for i in range(n):
            curr_height =heights[i]

            rightmost=i+1
            while rightmost<n and heights[rightmost]>=curr_height:
                rightmost+=1
            
            leftmost=i
            while leftmost>=0 and heights[leftmost]>=curr_height:
                leftmost-=1
            
            rightmost-=1
            leftmost+=1

            maxArea=max(maxArea,curr_height*(rightmost-leftmost+1))
        return maxArea