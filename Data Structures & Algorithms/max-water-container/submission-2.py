class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area=0
        l=0
        r=1
        while r < len(heights) and l<r:
            h = min(heights[l],heights[r])
            dist = r-l
            area = h * dist
            max_area = max(area,max_area)

            if r == len(heights)-1:
                l=l+1
                r=l+1
            else:
                r+=1
        return max_area
