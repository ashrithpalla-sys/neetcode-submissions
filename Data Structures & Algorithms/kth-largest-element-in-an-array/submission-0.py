class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq

        nums = [x * -1 for x in nums]
        heapq.heapify(nums)
        ans = 0

        for i in range(0, k):
            ans = heapq.heappop(nums)

        return ans * -1