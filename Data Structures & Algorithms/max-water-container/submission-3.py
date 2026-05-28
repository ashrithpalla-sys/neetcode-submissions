class Solution:
    def maxArea(self, heights: List[int]) -> int:
        a = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            left = heights[l]
            right = heights[r]
            curr = min(left, right) * (r-l)
            a = max(a, curr)

            if left < right:
                l += 1
            else:
                r -= 1

        return a
