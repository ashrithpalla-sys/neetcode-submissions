class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        used = set()
        for x in nums:
            if x in used:
                return True
            used.add(x)
        return False