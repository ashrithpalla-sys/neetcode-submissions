class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq

        if k == 0:
            return []

        freq_dict = {}
        for x in nums:
            if x in freq_dict:
                freq_dict[x] += 1
            else:
                freq_dict[x] = 1
        
        heap = [(value, key) for key, value in freq_dict.items()]
        heapq.heapify(heap)

        while len(heap) > k:
            heapq.heappop(heap)
        
        return [item[1] for item in heap]
