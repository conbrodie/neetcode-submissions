class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #  L             R
        # [1,7,2,5,4,7,3,6]
        # maxVol = 6, 30, 12
        l, r = 0, len(heights) - 1
        maxVolume = 0
        while l < r:
            maxVolume = max(maxVolume, min(heights[l], heights[r]) * (r - l))
            if heights[l] <= heights[r]:
                l += 1
            else: 
                r -= 1

        return maxVolume