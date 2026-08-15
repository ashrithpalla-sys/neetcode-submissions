class Solution:
    def tribonacci(self, n: int) -> int:
        one = 0
        two = 1
        three = 1
        temp = 2

        if n == 0:
            return one
        if n == 1:
            return two
        if n == 2:
            return three

        for i in range(4, n+2):
            temp = one + two + three
            one = two
            two = three
            three = temp

        return temp