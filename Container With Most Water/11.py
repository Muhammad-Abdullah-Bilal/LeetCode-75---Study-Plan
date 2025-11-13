class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_area = 0

        while l < r:
           hight = min(height[l], height[r])
           width = r - l
           area = hight * width
           max_area = max(max_area, area)
    
           if height[l] < height[r]:
              l += 1   # move left pointer right
           else:
              r -= 1   # move right pointer left

        return(max_area)
       
        