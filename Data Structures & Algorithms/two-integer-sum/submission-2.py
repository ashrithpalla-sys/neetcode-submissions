class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}

        for i, x in enumerate(nums):
            c = target - x
            if c in my_dict:
                return [my_dict[c], i]
            my_dict[x] = i