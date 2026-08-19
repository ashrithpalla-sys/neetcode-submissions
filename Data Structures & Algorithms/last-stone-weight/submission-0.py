class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq

        stones = [x * -1 for x in stones]
        heapq.heapify(stones)

        while len(stones) > 2:
            first = stones[0]
            second = min(stones[1], stones[2])
            heapq.heappop(stones)
            heapq.heappop(stones)

            if first < second:
                heapq.heappush(stones, first - second)
        
        if len(stones) == 2:
            return stones[1] - stones[0]
        
        return 0 if not stones else -stones[0]