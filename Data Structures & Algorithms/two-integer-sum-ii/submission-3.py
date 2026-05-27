class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        sum_pair_dict = {} 
    
        for i, x in enumerate(numbers):
            if x in sum_pair_dict: 
                return [sum_pair_dict[x] + 1, i + 1]
            sum_pair_dict[target - x] = i