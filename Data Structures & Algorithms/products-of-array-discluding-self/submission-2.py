class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        pref = 1
        suff = 1

        for i, x in enumerate(nums):
            output[i] = pref
            pref *= x

        for i in reversed(range(len(nums))):
            output[i] *= suff
            suff *= nums[i]

        return output