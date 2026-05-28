class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area=0
        l=0
        r=len(heights)-1
        while l<r:
            h = min(heights[l],heights[r])
            dist = r-l
            area = h * dist
            max_area = max(area,max_area)

            if heights[l] < heights[r]:
                l=l+1
            else:
                r-=1
        return max_area
