class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        l, r = 0, len(height) - 1
        while l != r:
            curr_area = min(height[l], height[r]) * (r - l)
            if max_area < curr_area:
                max_area = curr_area
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return max_area

        