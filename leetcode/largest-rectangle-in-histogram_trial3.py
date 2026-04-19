class Solution:
    def largestRectangleArea(self, heights):
        stack = []  
        
        maxarea = 0
        n = len(heights)

        for i in range(n):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                left = stack[-1] if stack else -1
                width = i - left - 1
                maxarea = max(maxarea, h * width)

            stack.append(i)

        while stack:
            h = heights[stack.pop()]
            left = stack[-1] if stack else -1
            width = n - left - 1
            maxarea = max(maxarea, h * width)

        return maxarea