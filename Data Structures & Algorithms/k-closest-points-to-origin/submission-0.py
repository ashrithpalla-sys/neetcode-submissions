class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        heap = []

        for [x, y] in points:
            d = (x ** 2 + y ** 2) ** 0.5

            if len(heap) < k:
                heapq.heappush(heap, (-d, [x,y]))
            else:
                heapq.heappushpop(heap, (-d, [x,y]))
        
        return [heapq.heappop(heap)[1] for _ in range(len(heap))]