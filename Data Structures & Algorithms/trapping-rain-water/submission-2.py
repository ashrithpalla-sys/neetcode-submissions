class Solution:
    def trap(self, height: List[int]) -> int:        
        prefix = [0 for i in range(len(height))]
        suffix = [0 for i in range(len(height))]

        p = 1
        s = len(height) - 2

        while p < len(height):
            if height[p - 1] > prefix[p - 1]:
                prefix[p] = height[p - 1]
            else:
                prefix[p] = prefix[p - 1]
            

            if height[s + 1] > suffix[s + 1]:
                suffix[s] = height[s + 1]
            else:
                suffix[s] = suffix[s + 1]

            p += 1
            s -= 1
        
        area = 0

        for i in range(len(height)):
            curr = min(prefix[i], suffix[i]) - height[i]
            
            if curr > 0:
                area += curr
        
        return area
        