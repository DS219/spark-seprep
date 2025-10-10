class Solution(object):
    def maxArea(self, heights):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        left, right = 0, len(heights) - 1
        while left < right: 
            area = min(heights[left],heights[right])*(right-left)
            if area > max_area: 
                max_area = area 
            if heights[left] >= heights[right]:
                right -= 1
            else:
                left += 1
        return max_area
        
