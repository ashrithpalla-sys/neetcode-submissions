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
                    j = stack[-1][0]
                    m = max(m, stack[-1][1]*(i-j))
                    stack.pop()
                stack.append((j, x))
        
        for i, h in stack:
            m = max(m, h*(len(heights)-i))
        
        return m