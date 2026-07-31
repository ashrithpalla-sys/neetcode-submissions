class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p, s in sorted(zip(position, speed), reverse=True)]
        times = []

        for p, s in pair:
            t = (target - p) / s

            if not times:
                times.append(t)
            elif t > times[-1]:
                times.append(t)
        
        return len(times)