class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        
        x_coords = [x for x, y in points]
        x_coords.sort()
        
        max_width = 0
        for i in range(1, len(x_coords)):
            max_width = max(max_width, x_coords[i] - x_coords[i-1])
        
        return max_width