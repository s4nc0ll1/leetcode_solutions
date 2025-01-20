"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        #Base cases
        if n == 1:
            return 1
            
        if n == 2:
            return 2

        #Variables
        a, b = 1, 2

        #Loop to explore previous steps
        for _ in range(3, n + 1):
            c = a + b
            a = b
            b = c
            
        return b # We return the sum of all possible previous attemps
        