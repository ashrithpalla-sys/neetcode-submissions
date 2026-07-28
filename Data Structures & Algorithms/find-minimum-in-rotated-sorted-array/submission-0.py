class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        l, r = 0, len(nums) - 1
        m = (l + r) // 2

        while m != l:
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
            
            m = (l + r) // 2
        
        return min(nums[l], nums[r])
            
        