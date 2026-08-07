class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        m = 0

        for i, x in enumerate(heights):
            if not stack:
                stack.append((i, x))
            else:
                j = i
                while stack and x < stack[-1][1]:
                    j, h = stack[-1][0], stack[-1][1]
                    stack.pop()
                    m = max(m, h * (i - j))
                stack.append((j, x))
        
        for i, h in stack:
            m = max(m, h * (len(heights) - i))
        
        return m