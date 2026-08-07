class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n

        two_back = 2
        one_back = 3

        for x in range(4, n+1):
            curr = one_back + two_back
            two_back = one_back
            one_back = curr

        return one_back