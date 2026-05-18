class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}

        for i, x in enumerate(nums):
            if x in my_dict:
                return [my_dict[x], i]
            my_dict[target - x] = i