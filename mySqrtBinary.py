"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        #Base cases
        if x < 2:
            return x
        
        left, rigth = 0 , x // 2

        while left <= rigth:
            mid = (left + rigth) // 2

            if mid * mid == x:
                return mid
            
            elif mid * mid > x :
                rigth = mid - 1
            
            else:
                left = mid + 1
        
        return rigth